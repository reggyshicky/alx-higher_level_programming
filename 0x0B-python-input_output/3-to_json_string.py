#!/usr/bin/python3
"""module documentation for json representation"""


import json


def to_json_string(my_obj):
    """
    function that uses json to convert data read from the text file
    to strings
    """
    return json.dumps(my_obj)
