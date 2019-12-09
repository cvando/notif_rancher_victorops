import requests
import json
import conf.default as cfg
import datetime

def firetovictorops(name, content, summary):
  url = 'https://api.victorops.com/api-public/v1/incidents'
  headers = {'content-type': 'application/json',
           'Accept': 'application/json',
           'X-VO-Api-Id': cfg.victorops_apid,
           'X-VO-Api-Key': cfg.victorops_apik
          }
  body = {
        "summary": summary,
        "details": content,
        "userName": cfg.victorops_username,
        "targets": [
            {
            "type": cfg.victorops_type,
            "slug": cfg.victorops_slug
            }
        ]
        }
  r = requests.post(url, data = json.dumps(body), headers=headers)
  if r.status_code == 200:
    jsondata = json.loads(r.text)
    issuename = jsondata['incidentNumber']
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(date+" POST msg vicotorops ok", flush=True)
    return (issuename)
  else :
    print("Bad victorops informations:", flush=True)
    print(r.text, flush=True)
    return (0)

def resolvetovictorops(issuename):
  url = 'https://api.victorops.com/api-public/v1/incidents/resolve'
  headers = {'content-type': 'application/json',
           'Accept': 'application/json',
           'X-VO-Api-Id': cfg.victorops_apid,
           'X-VO-Api-Key': cfg.victorops_apik
          }
  body = {
         "userName": cfg.victorops_username,
         "incidentNames": [
           issuename
         ],
         "message": "Autoresolved"
         }
  r = requests.patch(url, data = json.dumps(body), headers=headers)
  if r.status_code == 200:
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(date+" POST msg vicotorops ok", flush=True)
  else :
    print("Bad victorops informations:", flush=True)
    print(r.text, flush=True)