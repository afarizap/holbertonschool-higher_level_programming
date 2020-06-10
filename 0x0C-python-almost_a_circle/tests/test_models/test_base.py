#!/usr/bin/python3
""" test base class """


import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_base(unittest.TestCase):
    """ test base """
    def stup(self):
        """ for attributes """
        Base._Base__nb_objects = 0

    def test_not_run(self):
        """ fun test """
        print("no run")

    def test_object:(self):
        """ first test base """
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
