#!/usr/bin/python3
"""A modulue documentation for the shape rectangle"""


class Rectangle():
    """Defines a rectangle"""
    number_of_instances = 0  # public class attribute
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the class attributes"""

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with the greater area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise ValueError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new rectangl instance"""
        return (cls(size, size))

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
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
