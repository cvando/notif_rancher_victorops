import logging
import json
import sys
import os
import time
from dotenv import load_dotenv
from env_vars import env_files
from http.server import BaseHTTPRequestHandler, HTTPServer
from rancher import routing

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request "+str(self.path))
        self._set_response()
        self.wfile.write("ok".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(post_data)
        routing(post_data)
        logging.info("POST request "+str(self.path))
        self._set_response()
        self.wfile.write("ok".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8090):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
  while "CHANNELS" not in os.environ:
    env_files()
    time.sleep(1)
  print("Env vars loaded from env_vars", flush=True)

  from sys import argv
  if len(argv) == 2:
    run(port=int(argv[1]))
  else:
    run()