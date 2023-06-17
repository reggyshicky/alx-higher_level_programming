#!/usr/bin/python3
"""module documentation for a class Base"""


import json


class Base():
    """defines a class called Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """returns the json serialization of the list_objects"""
        file_name = cls.__name__ + ".json"

        with open(file_name, mode="w", encoding="utf-8") as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))
            list_dicts = []

            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())

            return f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """return a python obj from a json string"""
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """implements **dictionary as **kwargs using update mthd"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy_instance = cls(8, 8)
            if cls.__name__ == "Square":
                dummy_instance = cls(8)
            dummy_instance.update(**dictionary)
            return dummy_instance
