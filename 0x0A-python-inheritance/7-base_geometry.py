#!/usr/bin/python3
"""
module documentation for BaseGeometry
"""


class BaseGeometry():
    """defines the class BaseGeometry"""

    def area(self):
        """finds the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the type of value"""
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
