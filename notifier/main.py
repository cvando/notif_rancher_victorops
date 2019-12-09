import logging
import json
import sys
import os
import importlib
import conf.default as cfg
import time
from env_vars import env_files
from http.server import BaseHTTPRequestHandler, HTTPServer
from rancher import routing

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print("GET request "+str(self.path))
        self._set_response()
        self.wfile.write("ok".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        routing(post_data)
        print("POST request "+str(self.path))
        self._set_response()
        self.wfile.write("ok".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8090):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...\n', flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stopping httpd...\n')

if __name__ == '__main__':

  while "CHANNELS" not in os.environ:
    env_files()
    time.sleep(1)
  importlib.reload(cfg)
  print("Channels configured: "+cfg.channels, flush=True)

  from sys import argv
  if len(argv) == 2:
    run(port=int(argv[1]))
  else:
    run()