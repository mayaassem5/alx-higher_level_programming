#!/usr/bin/python3
import sys
length = len(sys.argv)
if length == 1:
    print("{} arguments.".format(length - 1))
else:
    print("{} arguments:".format(length - 1))

    for arg in range(1,length):
        print("{}: {}".format(arg, sys.argv[arg]))
