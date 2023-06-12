#!/usr/bin/python3
"""module documentation"""


class MyInt(int):
    """class that defines the subclass MyInt"""
    def __eq__(self, other):  # qe method used 4 equality comparsion(==)
        return super().__ne__(other)  # ne method 4 inequality " (!=)

    def __ne__(self, other):
        return super().__eq__(other)
