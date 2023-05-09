#!/usr/bin/python3
def remove_char_at(str, n):
    a_new_string = ""
    for d in range(len(str)):
        if d != n:
            a_new_string = a_new_string + str[d]
    return a_new_string
