#!/usr/bin/python3
""" Square inherited from rectangle """

from models.rectangle import Rectangle

class Square(Rectangle):

    """ And now the square """

    def __init__(self, size, x=0, y=0, id=None):
        
