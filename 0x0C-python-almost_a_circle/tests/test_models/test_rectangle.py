#!/usr/bin/python3
"""module documentation for testing the rectangle class"""
import unittest
import pep8
from models.base import Base
from models.base import Rectangle


class TestRectangle(unittest.TestCase):
    """A class to define the Rectangle test"""

    def test_pep8_Rectangle(self):
        style_checker = pep8.StyleGuide(quit=True)
        style_report = style_checker.check_files(['models/rectangle.py'])
        self.assertEqual(
            style_report.
