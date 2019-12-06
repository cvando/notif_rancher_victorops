import logging
import json
import sys
from env_vars import init_env_vars
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
    from sys import argv
    if init_env_vars() != 1:
      sys.exit(0)
      print("secrets Ko")
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
