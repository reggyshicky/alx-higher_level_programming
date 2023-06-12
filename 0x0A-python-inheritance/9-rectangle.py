#!/usr/bin/python3
"""module documentation"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines a subclass Rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """gives the area of  rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns str repr of a instance of class rectangle"""
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height)
