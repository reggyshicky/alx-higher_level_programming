#!/usr/bin/python3
for s in range(122, 96, -1):
    if s % 2 != 0:
        s = s - 32
    print("{}".format(chr(s)), end="")
