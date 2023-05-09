#!/usr/bin/python3
def uppercase(str):
    str_upper = ""
    for f in str:
        if ord(f) >= 97 and ord(f) <= 122:
            str_upper = str_upper + chr(ord(f) - 32)
        else:
            str_upper = str_upper + f
    print("{}".format(str_upper))
