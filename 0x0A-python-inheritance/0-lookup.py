#!/usr/bin/python3
"""Module documentation for lists of attributes and methods of an object"""


def lookup(obj):
    """Function that returns attr and methods of an object"""

    list_attr = []
    list_meth = []

    for names in dir(obj):
        userdefined = getattr(obj, names)
        if callable(userdefined):
            list_meth.append(names)
        else:
            list_attr.append(names)
    return list_attr + list_meth
