#!/usr/bin/python3
"""
Module documentation for checking the maximum integer
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaximumInteger(unittest.TestCase):
    """
    A class that defines the max_integer test
    """

    def test_max_integer(self):
        """
        function tests maximu integer in a list of +ve and -ve integers
        """
        self.assertIsNone(max_integer([]))
        self.assertAlmostEqual(max_integer([3, 4, 5, 6, 7]), 7)
        self.assertAlmostEqual(max_integer([-4, -3, -2, -1, 0]), 0)
        self.assertAlmostEqual(max_integer([-80, -130, -160, -190]), -80)
        self.assertAlmostEqual(max_integer([2.0, 2.5, 1.5, 3.8, 2.1]), 3.8)
        self.assertAlmostEqual(max_integer([5.5]), 5.5)

    def test_non_types(self):
        """
        Function that check what types are in the list
        """
        with self.assertRaises(TypeError):
            max_integer(None)

        with self.assertRaises(TypeError):
            max_integer(["Reggy", 78, 43, -4.5, "shicky"])
