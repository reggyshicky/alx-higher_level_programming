#!/usr/bin/python3
"""module documentation"""


def is_kind_of_class(obj, a_class):
    """
    returns true if obj is an instance of, or if the obj is an instance
    of a class that ingerited from, otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
