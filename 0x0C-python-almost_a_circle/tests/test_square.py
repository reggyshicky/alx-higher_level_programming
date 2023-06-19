#!/usr/bin/python3
"""Module for square class test cases"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """A testcase for class Square"""
    def test_base_pep8(self):
        """Checks the pycodestyle"""
        style_checker = pep8.StyleGuide(quit=True)
        style_report = style_checker.check_files(['models/square.py'])
        self.assertEqual(
            style_report.total_errors, 0,
            "Code style errors were found."
        )

    def test_getter(self):
        rect1 = Square(9)
        self.assertEqual(rect1.size, 9)

    def test_setter(self):
        rect1 = Square(9)
        rect1.size = 10
        self.assertEqual(rect1.size, 10)

    def test_str(self):
        rect1 = Square(4)

        with self.assertRaises(TypeError):
            rect1.size = "Re"

    def test_negative_size(self):
        rect1 = Square(5)

        with self.assertRaises(ValueError):
            rect1.size = -4

    def test_zero_size(self):
        rect1 = Square(6)

        with self.assertRaises(ValueError):
            rect1.size = 0

    def test_decimal_size(self):
        rect1 = Square(5)

        with self.assertRaises(TypeError):
            rect1.size = 2.5

    def test_tuple_size(self):
        rect1 = Square(5)

        with self.assertRaises(TypeError):
            rect1.size = (3, 9)

    def test_empty_size(self):
        rect1 = Square(6)

        with self.assertRaises(TypeError):
            rect1.size = ""

    def test_none_size(self):
        rect1 = Square(6)

        with self.assertRaises(TypeError):
            rect1.size = None

    def test_list_size(self):
        rect1 = Square(5)

        with self.assertRaises(TypeError):
            rect1.size = [5, 8]

    def test_dict_size(self):
        rect1 = Square(8)

        with self.assertRaises(TypeError):
            rect1.size = {"re": 5, "gerr": 8}

    def test_width_size(self):
        rect1 = Square(6)
        rect1.size = 7
        self.assertEqual(rect1.width, 7)
        self.assertEqual(rect1.height, 7)

    def test_to_dict(self):
        Base._Base__nb_objects = 0

        sq = Square(10, 2, 1, 9)
        sq_dict = sq.to_dictionary()
        result = {"id": 9, "x": 2, "size": 10, "y": 1}
        self.assertEqual(sq_dict, result)

        sq = Square(1, 0, 0, 9)
        sq_dict = sq.to_dictionary()
        result = {"id": 9, "x": 0, "size": 1, "y": 0}
        self.assertEqual(sq_dict, result)

        sq.update(6, 6, 6, 6)
        sq_dict = sq.to_dictionary()
        result = {"id": 6, "x": 6, "size": 6, "y": 6}
        self.assertEqual(sq_dict, result)
