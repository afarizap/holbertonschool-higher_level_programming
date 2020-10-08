#!/usr/bin/python3
""" Student to JSON """


class Student:
    """ defines a student by """

    def __init__(self, first_name, last_name, age):
        """ instantiation public """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves JSON representation of a student instance """
        new = self.__dict__.copy()
        if attrs and isinstance(attrs, list):
            for i in self.__dict__.keys():
                if i in attrs and type(i) is str:
                    continue
                else:
                    new.pop(i)
        return new
