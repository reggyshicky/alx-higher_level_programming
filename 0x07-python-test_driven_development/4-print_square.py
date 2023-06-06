#!/usr/bin/python3
"""
Module to print a square
"""


def print_square(size):
    """
    Function that prints a square with '#'
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
