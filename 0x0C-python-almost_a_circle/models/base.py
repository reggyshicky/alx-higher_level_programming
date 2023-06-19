#!/usr/bin/python3
"""module documentation for a class Base"""


import csv
from os import path
import json


class Base:
    """defines a class called Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class Base"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

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

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file_name = cls.__name__ + ".json"

        if path.exists(file_name) is False:  # checks if file exists
            return []
        with open(file_name, mode="r", encoding="utf-8") as f:
            python_objs = cls.from_json_string(f.read())
            list_instances = []

            for obj in python_objs:
                list_instances.append(cls.create(**obj))

            return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in csv"""
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    lstattr = ["id", "width", "height", "x", "y"]
                else:
                    lstattr = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=lstattr)
                for elem in list_objs:
                    writer.writerow(elem.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize csv to python object"""
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    lstattr = ["id", "width", "height", "x", "y"]
                else:
                    lstattr = ["id", "size", "x", "y"]
                py_dict = csv.DictReader(csvfile, fieldnames=lstattr)
                py_dict = [dict([k, int(v)] for k, v in dic.items())
                           for dic in py_dict]
                return [cls.create(**dic) for dic in py_dict]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles using the turtle module"""
        my_turt = turtle.Turtle()
        my_turt.screen.bgcolor("#7312c")
        my_turt.pensize(3)
        my_turt.shape("turtle")

        my_turt.color("#fffff")
        for rec in list_rectangles:
            my_turt.showturtle()
            my_turt.up()
            my_turt.goto(rec.x, rec.y)
            my_turt.down()
            for w in range(2):
                my_turt.forward(rec.width)
                my_turt.left(90)
                my_turt.forward(rec.height)
                my_turt.left(90)
            my_turt.hideturtle()

        my_turt.color("#b5e3d8")
        for sq in list_squares:
            my_turt.showturtle()
            my_turt.up()
            my_turt.goto(sq.x, sq.y)
            my_turt.down()
            for w in range(2):
                my_turt.forward(sq.width)
                my_turt.left(90)
                my_turt.forward(sq.height)
                my_turt.left(90)
            my_turt.hideturtle()

        turtle.exitonclick
