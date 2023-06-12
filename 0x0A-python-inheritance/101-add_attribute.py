#!/usr/bin/python3
"""module documentation"""


def add_attribute(obj, attr_name, attr_value):
    """a methond to add an attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr_name] = attr_value
