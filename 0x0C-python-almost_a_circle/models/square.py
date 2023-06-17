#!/usr/bin/python3
"""Module documentation for the class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the class Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrieves the width/size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of the size/width/height"""
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """update the key-worded and non-keyworded args accordingly"""
        len_args = len(args)
        len_kwargs = len(kwargs)
        names_of_attr = ["id", "size", "x", "y"]

        if len_args > 4:
            len_args = 4

        if len_args > 0:
            for w in range(len_args):
                setattr(self, names_of_attr[w], args[w])
        elif len_kwargs > 0:
            for key, value in kwargs.items():
                if key in names_of_attr:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns dict representation of a square"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
