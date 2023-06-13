#!/usr/bin/python3
"""module documentation for writing in a text file"""


def write_file(filename="", text=""):
    """
    function that writes a string in a text file and returns
    the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
