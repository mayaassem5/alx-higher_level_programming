#!/usr/bin/python3
for i in range(10):
    for x in range(i + 1, 10):
        if x == i:
            continue
        print("{}{}".format(i, x), end=", " if (i != 8 or x != 9) else "\n")
