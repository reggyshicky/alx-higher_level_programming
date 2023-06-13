#!/usr/bin/python3
"""module for appending a text to file"""


def append_write(filename="", text=""):
    """function that appends a text to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
