import json

import conf.default as cfg
from victorops import firetovictorops, resolvetovictorops
from citadel import firetocitadel

issues = []
tickets = {}

def routing(post_data):
  data = json.loads(post_data)
  try:
    status = data['status']
    date = data['alerts'][0]['labels']['event_firstseen']
    name = data['alerts'][0]['labels']['alert_name']
    msg = data['alerts'][0]['labels']['event_message']
    target = data['alerts'][0]['labels']['target_name']
    namespace = data['alerts'][0]['labels']['target_namespace']
    cluster = data['alerts'][0]['labels']['cluster_name']
    summary = cluster+" "+namespace+" "+name+" "+target
    content = "Status: "+status+"\nAlert: "+name+"\nFirst seen: "+date+"\nCluster: "+cluster+"\nNamespace: "+namespace+"\nTarget: "+name+"\nEvent: "+msg
    issue = [date, name, target]
    str = ' '.join(issue)
    varhash = hash(str)

    if status == "firing":
      if str not in issues:
        issues.append(str)
        if "victorops" in cfg.channels:
          tickets[varhash] = firetovictorops(name, content, summary)
        if "citadel" in cfg.channels:
          firetocitadel(content)
      
    if status == "resolved":
      for i in issues:
        if str == i:
          issues.remove(str)
          if "victorops" in cfg.channels:
            if varhash in tickets:
              numissue = tickets[varhash]
              resolvetovictorops(numissue)
              del tickets[varhash]
          if "citadel" in cfg.channels:
            firetocitadel(content)

  except KeyError:
    print("Malformed json") 


