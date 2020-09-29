#!/usr/bin/python3

""" This is a Rectangle """


class Rectangle:

    """ Here are the methods for Rectangle """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def width(self):
        return self.__width

    @wraps.width
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    def height(self):
        return self.__height

    @wraps.width
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
