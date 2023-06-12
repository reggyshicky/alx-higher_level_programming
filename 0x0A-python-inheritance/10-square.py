#!/usr/bin/python3
"""module documentation"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines subclass of Rectangle class"""

    def __init__(self, size):
        """initializes the Square class"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns the area of a square"""
        return self.__size * self.__size
