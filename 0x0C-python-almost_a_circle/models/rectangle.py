#!/usr/bin/python3
""" class Rectangle inherits from base """
from models.base import Base


class Rectangle(Base):
    """ Rectangle from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor call id from superclass assign args to att """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ Getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ Getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Return: area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ print Rectangle with # """
        [print() for i in range(self.__y)]
        for j in range(self.__height):
            [print(" ", end="") for i in range(self.__x)]
            [print("#", end="") for i in range(self.__width)]
            print()

    def __str__(self):
        """ String format of Rectangle attributes """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """ Update Rectangle attributes """
        n = len(args)
        if 0 in range(n):
            self.id = args[0]
        if 1 in range(n):
            self.width = args[1]
        if 2 in range(n):
            self.height = args[2]
        if 3 in range(n):
            self.x = args[3]
        if 4 in range(n):
            self.y = args[4]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary with Rectangle attributes """
        dictionary = {'id': self.id,
                      'width': self.width,
                      'height': self.height,
                      'x': self.x,
                      'y': self.y}

        return dictionary
