#!/usr/bin/python3

""" This is a Rectangle """


class Rectangle:

    """ Here are the methods for Rectangle """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        drawsqr = ""
        for i in range(0, self.height):
            if i != 0:
                drawsqr += "\n"
            for j in range(0, self.width):
                drawsqr += "#"
        return drawsqr

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
