#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import shutil

def run_cmd():
    os.environ["HOME"] = "/path/to/home"
    run_cmd = ('cd /path/to/repository && /usr/bin/php ./bin/satis build satis.json build')
    os.system(run_cmd)

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        self.wfile.write(run_cmd())

def run(server_class=HTTPServer, handler_class=S, port=YOUR_PORT):
    server_address = ('1.1.1.1', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd on host ', server_address[0], ' port ', server_address[1], '...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
