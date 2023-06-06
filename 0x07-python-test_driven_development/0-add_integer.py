#!/usr/bin/python3
"""
Module to add two integers
"""


def add_integer(a, b=98):
    """
    Adds two numbers which are float or int
    Casts float to integers then gives the solution
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
