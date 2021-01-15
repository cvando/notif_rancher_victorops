import json

import conf.default as cfg
from victorops import firetovictorops, resolvetovictorops
from citadel import firetocitadel

issues = []
tickets = {}

def routing(data):
  try:
    if 'status' in data:
      status = data['status']
      for alert in data['alerts']:
        # print("iter", flush=True) 
        # print(alert['labels']['alertname'], flush=True) 
        name = alert['labels']['alertname']
        cluster = alert['labels']['prometheus_from']
        date = alert['startsAt']
        target = json.dumps(alert['annotations'])
        namespace = alert['labels']['namespace']
  
  
        summary = cluster+" "+namespace+" "+name+" "+target
        content = "Status: "+status+"\nAlert: "+name+"\nFirst seen: "+date+"\nCluster: "+cluster+"\nNamespace: "+namespace+"\nTarget: "+name+" "+target
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
    print("Malformed json:", flush=True)
    print(data, flush=True) 


