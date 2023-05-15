#!/usr/bin/python3
def no_c(my_string):
    new_s = ""
    for char in my_string:
        if char not in ["c", "C"]:
            new_s = new_s + char
    return new_s
