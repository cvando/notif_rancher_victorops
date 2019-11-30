import requests
import json
import logging
import conf.default as cfg

def firetovictorops(name, msg, target):
  url = 'https://api.victorops.com/api-public/v1/incidents'
  body = {
        "summary": name+" "+target,
        "details": msg,
        "userName": cfg.myuserName,
        "targets": [
            {
            "type": cfg.mytype,
            "slug": cfg.slug
            }
        ]
        }
  r = requests.post(url, data = json.dumps(body), headers=headers)
  jsondata = json.loads(r.text)
  issuename = jsondata['incidentNumber']
  return (issuename)

def resolvetovictorops(issuename):
  url = 'https://api.victorops.com/api-public/v1/incidents/resolve'
  body = {
         "userName": cfg.myuserName,
         "incidentNames": [
           issuename
         ],
         "message": "Autoresolved"
         }
  r = requests.patch(url, data = json.dumps(body), headers=headers)


headers = {'content-type': 'application/json',
           'Accept': 'application/json',
           'X-VO-Api-Id': cfg.myapid,
           'X-VO-Api-Key': cfg.myapik
          }
