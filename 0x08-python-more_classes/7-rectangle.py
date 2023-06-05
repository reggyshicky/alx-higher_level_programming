#!/usr/bin/python3
"""Module representation for the shape rectangle"""


class Rectangle():
    """Defines the class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle attributes"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            solution = ""
            str_symbol = str(self.print_symbol)
            for row in range(self.__height - 1):
                solution += (str_symbol * self.__width) + '\n'
            solution += str_symbol * self.__width
        return solution

    def __repr__(self):
        h = str(self.__height)
        w = str(self.__width)
        solution = "Rectangle(" + w + ", " + h + ")"
        return solution

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
