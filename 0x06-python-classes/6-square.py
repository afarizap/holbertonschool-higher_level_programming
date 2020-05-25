#!/usr/bin/python3
""" area of square """


class Square:
    """ Definition of square area """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0 or value[1] is not True):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for y in range(0, self.position[1]):
                print()
            for i in range(0, self.size):
                for x in range(0, self.position[0]):
                    print(" ", end="")
                for j in range(0, self.size):
                    print("#", end="")
                print()
