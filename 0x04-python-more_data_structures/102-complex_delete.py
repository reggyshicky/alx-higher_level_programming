#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keysto_del = []
    for k, v in a_dictionary.items():
        if v == value:
            keysto_del.append(k)
    for k in keysto_del:
        del a_dictionary[k]
    return a_dictionary
