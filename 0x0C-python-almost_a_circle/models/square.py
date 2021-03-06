#!/usr/bin/python3
""" Square inherited from rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):

    """ And now the square """

    def __init__(self, size, x=0, y=0, id=None):
        """ imported attributes from Base """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string format of attributes in Square """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)

    @property
    def size(self):
        """ getter """
        return self.width or self.height

    @size.setter
    def size(self, size):
        """ Setter """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ update square attributes """
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

    def to_dictionary(self):
        """ store sttributes in dictionary """
        dictionary = {'id': self.id,
                      'size': self.size,
                      'x': self.x,
                      'y': self.y}
        return dictionary
