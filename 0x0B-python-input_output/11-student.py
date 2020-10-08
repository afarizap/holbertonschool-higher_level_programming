#!/usr/bin/python3
""" Student to JSON """


class Student:
    """ defines a student by """

    def __init__(self, first_name, last_name, age):
        """ instantiation public """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves JSON representation of a student instance """
        return self.__dict__
