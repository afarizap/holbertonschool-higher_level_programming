#!/usr/bin/python3
""" manage id attribute, to avoid duplicating the same code """


class Base:
    """ first class base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        if id is not None:
            self.id = None
        else:
            Base.__nb_objects +=1
            self.id = self.__nb_objects
