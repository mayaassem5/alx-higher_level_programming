#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    length = len(sys.argv)
    t = sys.argv[2]
    o = sys.argv[1]
    th = sys.argv[3]
    if length < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if t != "+" and t != "/" and t != "*" and t != "-":
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if t == "+":
                print("{} {} {} = {}".format(o, t, th, add(int(o), int(th))))
            elif t == "-":
                print("{} {} {} = {}".format(o, t, th, sub(int(o), int(th))))
            elif t == "/":
                print("{} {} {} = {}".format(o, t, th, div(int(o), int(th))))
            else:
                print("{} {} {} = {}".format(o, t, th, mul(int(o), int(th))))
