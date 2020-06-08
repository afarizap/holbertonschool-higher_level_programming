#!/usr/bin/python3
""" Square inherited from rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):

    """ And now the square """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)

    @property
    def size(self):
        return self.width or self.height

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
