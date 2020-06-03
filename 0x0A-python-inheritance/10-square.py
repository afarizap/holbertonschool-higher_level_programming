#!/usr/bin/python3
""" empty class """


class BaseGeometry:
    """ Base Geometry Class """
    def area(self):
        """ exception """
        raise Exception("area() is not implemented Exception")

    def integer_validator(self, name, value):
        """ validate if value is an in """
        if type(value) is not int:
            raise TypeError ("<name> must be an integer")
        if value <= 0:
            raise ValueError ("<name> must be greater than 0")

class Rectangle(BaseGeometry):
    """ Rectangle Class """


    def __init__(self, width, height):
        """ validate and private values """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ print legible rectangle fields """
        a = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return a

class Square(Rectangle):
    """ Square Class """


    def __init__(self, size):
        """ instatation size """
        self.integer_validator("size", size)
        self.__size = size

    def area(self, size):
        """ area method """
        return super.area
