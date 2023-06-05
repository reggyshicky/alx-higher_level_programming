#!/usr/bin/python3
"""module documentation"""


class Rectangle():
    """Defines a class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initiliazes the class Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            solution = ""
            for w in range(self.__height - 1):
                solution += ("#" * self.__width) + '\n'
            solution += "#" * self.__width
        return solution

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
