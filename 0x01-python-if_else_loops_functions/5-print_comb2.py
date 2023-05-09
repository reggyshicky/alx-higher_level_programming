#!/usr/bin/python3
for v in range(0, 100):
    if v < 99:
        print("{:02d}, ".format(v), end='')
    else:
        print("{:02d}".format(v))
