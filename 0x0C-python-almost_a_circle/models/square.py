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

    def update(self, *args, **kwargs):
        n = len(args)

        if 0 in range(n):
            self.id = args[0]
        if 1 in range(n):
            self.size = args[1]
        if 2 in range(n):
            self.x = args[2]
        if 3 in range(n):
            self.y = args[3]

        if n is not 0:
            pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
