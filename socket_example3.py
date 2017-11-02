#!/usr/bin/python3
import os
import re
from socket import *

server = '10.10.10.10' # IP or hostname
listen_port = 5775

class Srvstat:
    def connect(self, host = server, port = listen_port):
        self.socket = socket(AF_INET, SOCK_STREAM)          # For local access use AF_UNIX
        self.socket.bind((host, port))
        self.socket.listen(5)

    def process(self):

        while True:
            try:
                csocket, caddress = self.socket.accept()
                csocket.send('Connection established. Please input your request.\n'.encode())

            except TypeError:
                raise
                self.socket.detach()
                self.socket.close()

            while True:
                request = csocket.recv(64)
                if re.match('get\s+ifstat'.encode(), request, re.IGNORECASE):
                    csocket.send(str(os.popen('/sbin/ifconfig').read()).encode())
                elif re.match('quit'.encode(), request, re.IGNORECASE):
                    break
                else:
                    csocket.send('Unknown command.\n')
                    csocket.close()

if __name__ == '__main__':
    serv = Srvstat()
    serv.connect()
    serv.process()



"""
For use:
 - start script
 - telnet from remote host on defined port and ip
 - and input command: get ifstat
"""
