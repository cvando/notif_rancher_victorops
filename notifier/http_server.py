from klein import run, route
from rancher import routing
import json

def listen():
  @route('/', methods=['POST'])
  def do_post(request):
    content = json.loads(request.content.read())
    response = "ok"
    routing(content)
    return response
  
  @route('/healthz')
  def check(request):
    return "Ok"

  run("0.0.0.0", 8090)