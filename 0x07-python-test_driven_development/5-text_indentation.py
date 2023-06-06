#!/usr/bin/python3
"""
module to print 2 new lines after few special characters
"""


def text_indentation(text):
    """
    Function that prints text with two lines after '.', '?', ':'
    """
    if isinstance(text, str) is not True:
        raise TypeError("text must be a string")
    new_str = text.split()
    new_str = " ".join(new_str)
    new_str = new_str.replace(".", ".\n\n")
    new_str = new_str.replace(":", ":\n\n")
    new_str = new_str.replace("?", "?\n\n")
    new_str = new_str.replace("\n ", "\n")

    print(new_str, end='')
