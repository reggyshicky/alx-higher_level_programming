#!/usr/bin/python3
"""module documentation for testing the rectangle class"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """A class to define the Rectangle test"""

    def test_pep8_Rectangle(self):
        style_checker = pep8.StyleGuide(quit=True)
        style_report = style_checker.check_files(['models/rectangle.py'])
        self.assertEqual(
            style_report.total_errors, 0,
            "Code style errors were found."
        )

    def test_subcls_rectangle(self):
        """
        Testing functionality of the subclass
        rectangle regarding the superclass Base
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_args(self):
        """Test the class Rectangle parameters"""
        rect1 = Rectangle(10, 2)
        rect2 = Rectangle(2, 10)
        rect3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(rect1.id, 3)
        self.assertEqual(rect1.width, 10)
        self.assertEqual(rect1.height, 2)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)
        self.assertEqual(rect2.id, 4)
        self.assertEqual(rect2.width, 2)
        self.assertEqual(rect2.height, 10)
        self.assertEqual(rect2.x, 0)
        self.assertEqual(rect2.y, 0)
        self.assertEqual(rect3.id, 12)
        self.assertEqual(rect3.width, 10)
        self.assertEqual(rect3.height, 2)
        self.assertEqual(rect3.x, 0)
        self.assertEqual(rect3.y, 0)

        with self.assertRaises(TypeError):
            r4 = Rectangle()

    def test_str_param(self):
        """Test str params of the Rectangle class"""
        with self.assertRaises(TypeError):
            Rectangle("Reggy", "Python")

    def test_paramtypes(self):
        """Test for class Rectangle types of parameters"""
        with self.assertRaises(TypeError):
            Rectangle(2.06, 3)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(-543345543, 45)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle('', 8)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(8, 34.67)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(10, "Reggy")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(9, True)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(4, -44553483598)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle(6, 3, 1.25)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(7, 9, "reggy")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(6, 10, True)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(10, 15, -5834394523)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle(6, 8, 5, "reggy")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(6, 8, True)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(6, 8, 6, -4483845868)
            raise ValueError()
