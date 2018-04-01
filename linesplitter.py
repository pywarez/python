#!/usr/bin/python
import sys
myfile = sys.argv[1]
f = open(myfile, "r")
myfile = f.readlines()
emptystring = ""
for line in myfile:
    line = line.strip("\r\n")
    emptystring += line
print emptystring
