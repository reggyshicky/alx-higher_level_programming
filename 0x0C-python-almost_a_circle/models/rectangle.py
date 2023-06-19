#!/usr/bin/python3
"""module documentation for class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Define the class Rectangle inheriting from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class Rectangle"""
        super().__init__(id)

        self.validate_param(width, "width")
        self.validate_param(height, "height")
        self.validate_param(x, "x")
        self.validate_param(y, "y")

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
        """sets the width of the rectangle"""
        self.validate_param(value, "width")
        self.__width = value

    @property
    def height(self):
        """retrieves the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height value"""
        self.validate_param(value, "height")
        self.__height = value

    @property
    def x(self):
        """retrieves the x coordinates"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x coordinates"""
        self.validate_param(value, "x")
        self.__x = value

    @property
    def y(self):
        """retrieves the y coordinates"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y coordinates"""
        self.validate_param(value,  "y")
        self.__y = value

    def validate_param(self, param, value):
        """Validates width, height, x and y"""
        if type(param) is not int:
            raise TypeError(value + ' must be an integer')
        if param <= 0 and value in ("width", "height"):
            raise ValueError(value + " must be > 0")
        if param < 0 and value in ("x", "y"):
            raise ValueError(value + " must be >= 0")

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

    def update(self, *args, **kwargs):
        """use for passing args using *args and *kwargs"""
        len_args = len(args)
        len_kwargs = len(kwargs)
        names_of_attr = ["id", "width", "height", "x", "y"]

        if len_args > 5:
            len_args = 5
        if len_args > 0:
            for w in range(len_args):
                setattr(self, names_of_attr[w], args[w])
        elif len_kwargs > 0:
            for key, value in kwargs.items():
                if key in names_of_attr:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of Class Rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
