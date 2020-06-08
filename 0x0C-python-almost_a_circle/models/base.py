#!/usr/bin/python3
""" manage id attribute, to avoid duplicating the same code """
import json


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

    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        with open("cls.json", "a", encoding="utf-8") as f:
            f.write("holi")
