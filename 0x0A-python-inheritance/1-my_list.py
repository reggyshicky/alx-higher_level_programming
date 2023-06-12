#!/usr/bin/python3
"""A module documentation that creates subclass using superclass"""


class MyList(list):
    """Defines a subclass of a superclass list"""

    def print_sorted(self):
        """prints a list in ascending order"""
        print(sorted(self))
