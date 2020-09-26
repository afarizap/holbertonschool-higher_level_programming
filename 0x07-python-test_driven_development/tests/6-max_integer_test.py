#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty(self):
        """ test max integer when empty list given"""
        self.assertEqual(max_integer([]), None)

    def test_is_int(self):
        """ test if the given arg is an int """
        self.assertIs(type(max_integer([1])), int)
        self.assertIs(type(max_integer([a])), int)
