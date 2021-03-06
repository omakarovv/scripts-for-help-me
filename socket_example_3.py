#!/usr/bin/python3

import os
import re
from socket import *

server = '192.168.1.55' # IP or hostname
listen_port = 5775

class remote_control:

    def __init__(self, host = server, port = listen_port):
        self.socket = socket(AF_INET, SOCK_STREAM)          # For local access use AF_UNIX
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.socket.bind((host, port))
        self.socket.listen(2)
#        print ("Server started on: Host" + " " +
#              str(self.socket.getsockname()[0]) + " and port" + " " + str(self.socket.getsockname()[1]))
        print(self.socket)

    def process(self):
        while True:
            try:
                csocket, caddress = self.socket.accept()
                self.local_worker(csocket)
            except TypeError:
                raise

    def local_worker(self, csocket):
        csocket.send('Connection established on. Please input your request.\n'.encode())
        while True:
            request = csocket.recv(4096)
            print(request)
            if re.match('get\s+ifstat'.encode(), request, re.IGNORECASE):
                csocket.send(str(os.popen('/sbin/ifconfig').read()).encode())
            elif re.match('quit'.encode(), request, re.IGNORECASE):
                csocket.send('Good bye.\n'.encode())
                csocket.close()
                break
            else:
                csocket.send('Unknown command.\n'.encode())

if __name__ == '__main__':
    remote_access = remote_control()
    try:
#        remote_access.connect()
        remote_access.process()
    except KeyboardInterrupt:
        print('\n','Server stopped')



"""
It's example script.
For use:
 - start script on the server
 - telnet from remote host on defined port and ip
 - and input command: get ifstat
"""
