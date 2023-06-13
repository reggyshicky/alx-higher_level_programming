#!/usr/bin/python3
"""Module documentation for json return of python data"""


import json


def from_json_string(my_str):
    """
    function that returns a python object represented by
    python string
    """
    return json.loads(my_str)
