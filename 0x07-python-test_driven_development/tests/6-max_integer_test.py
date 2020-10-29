#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ here start unit test functions """

    def test_empty(self):
        """ test max integer when empty list given"""
        self.assertEqual(max_integer([]), None)

    def test_is_int(self):
        """ test if the given arg is an int """
        self.assertIs(type(max_integer([1])), int)

    def max_at_the_end(self):
        """ test if there is a max in the end of the list"""
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)
