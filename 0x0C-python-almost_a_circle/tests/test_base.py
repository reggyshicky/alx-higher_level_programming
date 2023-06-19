#!/usr/bin/python3
"""
A module documentation for implementing a
unittest to the Base Class
"""
import unittest
import os
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Defines the test for the class Base"""

    def test_pep8_compliance(self):
        """Tests pycodestyle"""
        style_checker = pep8.StyleGuide(quit=True)
        style_report = style_checker.check_files(['models/base.py'])
        self.assertEqual(
            style_report.total_errors, 0,
            "Code style errors were found."
        )

    def test_positive_id(self):
        """Tests for a +ve id of the base class"""
        basecls_instance = Base(54)
        self.assertEqual(basecls_instance.id, 54)
        basecls_instance = Base(75)
        self.assertEqual(basecls_instance.id, 75)

    def test_negative_id(self):
        """Tests for -ve id of the base class"""
        basecls_instance = Base(-32)
        self.assertEqual(basecls_instance.id, -32)
        basecls_instance = Base(-13)
        self.assertEqual(basecls_instance.id, -13)

    def test_no_id(self):
        """Test for a None id"""
        basecls_instance = Base(None)
        self.assertEqual(basecls_instance.id, 2)

    def test_str_id(self):
        basecls_instance = Base("Reggy Shicky")
        self.assertEqual(basecls_instance.id, "Reggy Shicky")
        basecls_instance = Base("I like Avocado")
        self.assertEqual(basecls_instance.id, "I like Avocado")

    def test_to_json_str(self):
        """Test to json string function"""
        instance_Rect = Rectangle(16, 10, 4, 9, 45)
        rect_data = instance_Rect.to_dictionary()
        json_data = Base.to_json_string([rect_data])
        self.assertEqual(type(json_data), str)

    def test_to_json_str_emptyarg(self):
        """Test if passed list_dictionaries is empty"""
        empty_list = []
        json_data = Base.to_json_string(empty_list)
        self.assertEqual(json_data, "[]")

        None_list = None
        json_data = Base.to_json_string(None_list)
        self.assertEqual(json_data, "[]")

    def test_base_instance(self):
        """Test to check for a base instance"""
        basecls_instance = Base()
        self.assertEqual(type(basecls_instance), Base)
        self.assertTrue(isinstance(basecls_instance, Base))

    def test_to_json_str_normal_working(self):
        """Test how the function to for json works"""
        rect_dict = {'id': 23, 'x': 24, 'y': 21, 'width': 10, 'height': 8}
        json_dict = Base.to_json_string([rect_dict])

        self.assertTrue(isinstance(rect_dict, dict))
        self.assertTrue(isinstance(json_dict, str))
        self.assertCountEqual(
            json_dict,
            '{["id": 23, "x": 24, "y": 21, "width": 10, "height": 8]}'
        )

    def test_to_json_str_wrong_working(self):
        """tests if json function does not work correctly"""
        json_data = Base.to_json_string(None)
        self.assertEqual(json_data, "[]")

        erro = ("to_json_string() missing 1 required positional argument: " +
                "'list_dictionaries'")

        with self.assertRaises(TypeError) as err_msg:
            Base.to_json_string()

        self.assertEqual(erro, str(err_msg.exception))

        err = "to_json_string() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as err_msg:
            Base.to_json_string([{24, 56}], [{32, 12}])

        self.assertEqual(err, str(err_msg.exception))

    def test_save_to_file_wrongly(self):
        """Tests the save to file function functionality"""
        with self.assertRaises(AttributeError) as err_msg:
            Base.save_to_file([Base(1), Base(2)])

        self.assertEqual(
            "'Base' object has no attribute 'to_dictionary'",
            str(err_msg.exception)
        )

    def test_load_from_file(self):
        """Tests the deserialization"""
        if os.path.exists("Base.json"):
            os.remove("Base.json")

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

        rect_result = Rectangle.load_from_file()
        self.assertEqual(rect_result, [])

        square_result = Square.load_from_file()
        self.assertEqual(square_result, [])

        err = "load_from_file() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as err_msg:
            Rectangle.load_from_file('Reggy Shicky')

        self.assertEqual(err, str(err_msg.exception))

    def test_create_args_kwargs(self):
        """Test the create methond"""
        with self.assertRaises(TypeError) as err_msg:
            err = Rectangle.create('Reggy Shicky')

        self.assertEqual(
            "create() takes 1 positional argument but 2 were given",
            str(err_msg.exception)
        )
