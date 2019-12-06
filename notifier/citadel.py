import requests
import json
import conf.default as cfg
import datetime

def citadellogin():
  url = cfg.citadel_url+'/_matrix/client/r0/login'
  body = {
         "address": cfg.citadel_email,
         "type": "m.login.password",
         "identifier": {
           "type": "m.id.thirdparty",
           "address": cfg.citadel_email,
           "medium": "email"
           },
         "medium": "email",
         "password": cfg.citadel_password,
         "initial_device_display_name": "NUXBOT"
        }
  headers = {'content-type': 'application/json',
            'Accept': 'application/json',
            }
  r = requests.post(url, data = json.dumps(body), headers=headers)
  if r.status_code == 200:
    jsondata = json.loads(r.text)
    token = jsondata['access_token']
    return (token)
  else:
    return(0)

def citadelpost(token, content):
  url = cfg.citadel_url+'/_matrix/client/r0/rooms/'+cfg.citadel_room_id+'/send/m.room.message/35'
  body = {
         "msgtype": "m.text",
         "body": content
         }
  headers = {'content-type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'Bearer '+token,
            }
  r = requests.put(url, data = json.dumps(body), headers=headers)

def citadellogout(token):
  url = cfg.citadel_url+'/_matrix/client/r0/logout/all'
  headers = {'content-type': 'application/json',
            'Accept': 'application/json',
            'authorization': 'Bearer '+token,
            }
  r = requests.post(url, headers=headers)

def firetocitadel(content):
  now = datetime.datetime.now()
  date = now.strftime("%Y-%m-%d %H:%M:%S")
  token = citadellogin()
  if token == 0:
    print(date+" POST Login error")
  else:
    citadelpost(token, content)
    citadellogout(token)
    print(date+" POST msg citadel ok")