#!/usr/bin/python3
"""module documentation for use of load, python object creation"""


import json


def load_from_json_file(filename):
    """functon that creates an Object from a Json file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
