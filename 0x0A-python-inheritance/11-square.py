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
        m = "[{}] {}/{}".format(__class__.__name__,
                                self.__width, self.__height)
        return m


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ instatation size """
        Rectangle.__init__(self, size, size)
        self.integer_validator("size", size)
        self.__size = size
        self.__width = size
        self.__height = size

    def area(self):
        """ area method """
        return super().area()

    def __str__(self):
        """ print legible rectangle fields """
        m = "[{}] {}/{}".format(__class__.__name__,
                                self.__width, self.__height)
        return m

if __name__ == "__main__":
    import doctest

    doctest.testfile("./tests/7-base_geometry.txt")
