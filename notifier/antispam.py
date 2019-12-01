import json
import logging
import conf.default as cfg
from victorops import firetovictorops, resolvetovictorops

issues = []
tickets = {}

def routing(post_data):
  data = json.loads(post_data)
  if data['alerts'] is not None:
    status = data['status']
    date = data['alerts'][0]['labels']['event_firstseen']
    name = data['alerts'][0]['labels']['alert_name']
    msg = data['alerts'][0]['labels']['event_message']
    target = data['alerts'][0]['labels']['target_name']
    issue = [date, name, target]
    str = ' '.join(issue)
    varhash = hash(str)

    if status == "firing":
      if str not in issues:
        issues.append(str)
        if "victorops" in cfg.channels:
          tickets[varhash] = firetovictorops(name, msg, target)
        logging.info("fire "+str)

    if tickets[varhash] is not None:
      if status == "resolved":
        for i in issues:
          if str == i:
            issues.remove(str)
            if "victorops" in cfg.channels:
              resolvetovictorops(tickets[varhash])
            logging.info("resolve "+str)
          del tickets[varhash]
