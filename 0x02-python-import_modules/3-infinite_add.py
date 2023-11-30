#!/usr/bin/python3
import sys
if __name__=="__main__":
    length = len(sys.argv)
    add = 0
    for arg in range(1, length):
        add += int(sys.argv[arg])
    print("{}".format(add))
