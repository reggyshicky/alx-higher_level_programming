#!/usr/bin/python3
"""module documentation for class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Define the class Rectangle inheriting from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class Rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets thw width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieves the x coordinates"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x coordinates"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieves the y coordinates"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y coordinates"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """function that calculates the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """function that displays the # in form of rectangle"""
        if self.__y > 0:
            print('\n' * self.__y, end="")

        for w in range(self.height):
            if self.__x > 0:
                print(" " * self.__x, end="")

            print("#" * self.__width)

    def __str__(self):
        """returns a human-readable description of class attributes"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.x, self.y, self.width, self.height)
