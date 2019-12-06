import requests
import json
import conf.default as cfg

def firetovictorops(name, content, summary):
  url = 'https://api.victorops.com/api-public/v1/incidents'
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
    return (issuename)
  else :
    print("Bad victorops informations")
    return (0)

def resolvetovictorops(issuename):
  url = 'https://api.victorops.com/api-public/v1/incidents/resolve'
  body = {
         "userName": cfg.victorops_username,
         "incidentNames": [
           issuename
         ],
         "message": "Autoresolved"
         }
  r = requests.patch(url, data = json.dumps(body), headers=headers)


headers = {'content-type': 'application/json',
           'Accept': 'application/json',
           'X-VO-Api-Id': cfg.victorops_apid,
           'X-VO-Api-Key': cfg.victorops_apik
          }
