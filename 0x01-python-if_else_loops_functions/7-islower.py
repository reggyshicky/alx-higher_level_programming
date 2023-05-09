#!/usr/bin/python3
def islower(c):
    codeAscii = ord(c)

    if (codeAscii >= 97 and codeAscii <= 122):
        return True
    else:
        return False
