#!/usr/bin/python3
"""module documentation of reading a textfile"""


def read_file(filename=""):
    """function that reads a text file and prints to stdout"""
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            print("{}".format(line), end="")
