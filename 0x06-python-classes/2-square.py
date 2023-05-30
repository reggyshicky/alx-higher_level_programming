#!/usr/bin/python3
"""
module documentation
"""


class Square():
    """
    A class that defines a square
    """

    def __init__(self, size=0):
        """
        Initializes a square instance/object

        Args:
             size (int, optional: The size of the square.Defaults to 0
                  Raises a TypeError if size is not an integer
                  Raises a Value Error if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
