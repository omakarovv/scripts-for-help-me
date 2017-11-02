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
        server_info = self.socket.getsockname()
        print ("Server started on: Host" + " " +
               str(server_info[0]) + " and port" + " " + str(server_info[1]))

    def process(self):

        while True:
            try:
                csocket, caddress = self.socket.accept()
                csocket.send('Connection established on. Please input your request.\n'.encode())


            except TypeError:
                raise

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
 - start script on the server
 - telnet from remote host on defined port and ip
 - and input command: get ifstat
"""
