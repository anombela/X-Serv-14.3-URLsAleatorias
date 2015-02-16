#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Simple HTTP Server: reuses the port, so it can be
restarted right after it has been killed. Accepts connects from
the outside world, by binding to the primary interface of the host.
"""

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind((socket.gethostname(), 1234))
mySocket.listen(5)


try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'Request received:'
        print recvSocket.recv(2048)
        print 'Answering back...'
        recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body>Hola." +
                        "<a href=" +
                        str(random.randint(0, 10000000)) +
                        ">Dame Otra!!" +
                        "</p>" +
                        "</body></html>" +
                        "\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
