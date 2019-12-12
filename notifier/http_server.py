from klein import run, route
from rancher import routing
import json

def listen():
  @route('/', methods=['POST'])
  def do_post(request):
    content = json.loads(request.content.read())
    response = "ok"
    print(content, flush=True)
    routing(content)
    return response
  run("localhost", 8080)