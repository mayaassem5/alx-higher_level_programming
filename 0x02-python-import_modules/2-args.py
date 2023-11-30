#!/usr/bin/python3
import sys
length = len(sys.argv)
if length == 1:
    print("{} arguments.".format(length - 1))
elif length == 2:
    print("{} argument:".format(length - 1))
    print("1: {}".format(sys.argv[1]))
else:
    print("{} arguments:".format(length - 1))

    for arg in range(1,length):
        print("{}: {}".format(arg, sys.argv[arg]))
