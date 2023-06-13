#!/usr/bin/python3
"""module documentation"""


def class_to_json(obj):
    """
    function that returns a dictionary description
    for json serialization
    """
    return obj.__dict__
