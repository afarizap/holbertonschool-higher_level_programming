#!/usr/bin/python3
""" empty class """


class BaseGeometry:
    """ Base Geometry Class """
    def area(self):
        raise Exception("area() is not implemented Exception")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError ("<name> must be an integer")
        if value <= 0:
            raise ValueError ("<name> must be greater than 0")

class Rectangle(BaseGeometry):
    """ Rectangle Class """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height