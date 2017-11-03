#!/usr/bin/python3

import os
import re
from socket import *

server = '192.168.1.55' # IP or hostname
listen_port = 5775

class Srvstat:

    def connect(self, host = server, port = listen_port):
        self.socket = socket(AF_INET, SOCK_STREAM)          # For local access use AF_UNIX
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.socket.bind((host, port))
        self.socket.listen(5)
#        print ("Server started on: Host" + " " +
#              str(self.socket.getsockname()[0]) + " and port" + " " + str(self.socket.getsockname()[1]))
        print(self.socket)

    def process(self):

        while True:
            try:
                csocket, caddress = self.socket.accept()
                csocket.send('Connection established on. Please input your request.\n'.encode())


            except TypeError:
                raise

            while True:
                request = csocket.recv(1024)
                print(request)
                if re.match('get\s+ifstat'.encode(), request, re.IGNORECASE):
                    csocket.send(str(os.popen('/sbin/ifconfig').read()).encode())
                elif re.match('quit'.encode(), request, re.IGNORECASE):
                    self.socket.shutdown(SHUT_WR)
                    self.socket.close()


                else:
                    csocket.send('Unknown command.\n'.encode())


if __name__ == '__main__':
    serv = Srvstat()
    serv.connect()
    serv.process()



"""
It's example script.
For use:
 - start script on the server
 - telnet from remote host on defined port and ip
 - and input command: get ifstat
"""
