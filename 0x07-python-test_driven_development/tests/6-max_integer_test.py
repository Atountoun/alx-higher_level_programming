#!/usr/bin/python3
"""This module contains unittest class for max_integer function."""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class is for test cases of function max_integer."""

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_negative_max(self):
        self.assertEqual(max_integer([-6, -2, -9, -4, -14, -2, -1]), -1)
        self.assertEqual(max_integer([-5, -11, -9, -8, -10, -43, -6]), -5)

    def test_positive_max(self):
        self.assertEqual(max_integer([5, 0, 2, 8, 1, 4, 9, 3, 9, 13]), 13)
        self.assertEqual(max_integer([10, 12, 18, 11, 14, 12, 29, 10]), 29)

    def test_positive_and_negative_max(self):
        self.assertEqual(max_integer([5, 2, -1, -2, 9, 15, -22, 30, -14]), 30)
        self.assertEqual(max_integer([4, 2, 10, 6, -2, -1, 15, -20, 11]), 15)
