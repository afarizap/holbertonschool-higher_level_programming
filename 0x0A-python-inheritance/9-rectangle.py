#!/usr/bin/python3
""" empty class """


class BaseGeometry:
    """ Base Geometry Class """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle Class """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ print legible rectangle fields """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

if __name__ == "__main__":
    import doctest

    doctest.testfile("./tests/7-base_geometry.txt")
