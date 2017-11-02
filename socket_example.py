#!/usr/bin/python
import os
import re
from socket import *

server = '10.10.10.10' # IP or hostname
listen_port = 5775

class Srvstat:
    def __init__(self, host=server, port = listen_port):
        self.socket = socket(AF_INET, SOCK_STREAM)          # For local access use AF_UNIX
        self.socket.bind((host, port))
        self.socket.listen(5)
    def process(self):
        while True:
            csocket, caddress = self.socket.accept()
            csocket.send('Connection established. Please input your request.\n')
            while True:
                request = csocket.recv(64)
                if re.match('get\s+ifstat', request, re.IGNORECASE):
                     csocket.send(os.popen('/sbin/ifconfig').read())
                elif re.match('quit', request, re.IGNORECASE):
                    break
                else:
                    csocket.send('Unknown command.\n')
                    csocket.close()

if __name__ == '__main__':
    serv = Srvstat()
    serv.process()

"""
For use:
 - start script
 - telnet from remote host on defined port and ip
 - and input command: get ifstat
"""
