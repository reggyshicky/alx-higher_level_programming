#!/usr/bin/python3
"""module documentation"""


class Student():
    def __init__(self, first_name, last_name, age):
        """Initialization of the class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns the dictionary representation
        of student instance
        """
        try:
            for elem in attrs:
                if type(elem) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        the_dict = dict()
        for key, value in self.__dict__items():
            if key in attrs:
                the_dict[key] = value
        return the_dict

    def reload_from_json(self, json):
        """replaces all attributes of the student instance"""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
