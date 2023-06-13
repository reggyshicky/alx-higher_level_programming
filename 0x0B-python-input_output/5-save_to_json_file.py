#!/usr/bin/python3
"""module documentationg for opening and writing a file using json"""


import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an object to a text file
    using json representation
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
