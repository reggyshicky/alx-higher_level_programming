#!/usr/bin/python3
"""module documentation for use of load, python object creation"""


import json


def load_from_json_file(filename):
    """functon that creates an Object from a Json file"""
    with open(filename, "w") as f:
        return json.loads(f)
