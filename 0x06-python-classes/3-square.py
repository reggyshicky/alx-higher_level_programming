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
        Initializes a Square Instance

        Args:
            size (int, optional): The size of the square.Defauts to zero.
            Raises a TyperError if size is not an integer
            Raises a ValueError if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates and returns th area of a square.

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
