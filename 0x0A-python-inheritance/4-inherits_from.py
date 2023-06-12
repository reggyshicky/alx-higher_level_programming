#!/usr/bin/python3
"""module documentation"""


def inherits_from(obj, a_class):
    """
    returns true if an obj is an istance of a class that inherited(directly)
    or indirectly from a specified class
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class


"""
the issubclass is used to check ig the class of the object type(obj) is a
subclass of the specified class(a_class), the 2nd part is used to ensure that
the object's class is not the same as the specified class, this is neccessary
to exclude cases where the object's class is exactly the same as a_class
"""
