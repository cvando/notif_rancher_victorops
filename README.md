# Notifier rancher victorops citadel

<br>

### Description

Simple webserver waiting for json

<br>

### Json

json example with mandatory fields :

{"status":"firing","alerts":[{"status":"firing","labels":{"alert_name":"Get warning deployment event","cluster_name":"mycluster","event_firstseen":"2019-11-29 23:42:18 +0000 UTC","event_message":"Readiness probe failed: HTTP probe failed with statuscode: 503","target_name":"mypod","target_namespace":"mynamespace"}}]}

<br>

### Configuration env vars

CHANNELS = "vicotorops citadel" #output enabled if present

VICTOROPS_USERNAME
VICTOROPS_TYPE
VICTOROPS_SLUG
VICTOROPS_API_ID
VICTOROPS_API_KEY

CITADEL_URL
CITADEL_EMAIL
CITADEL_PASSWORD
CITADEL_ROOM_ID