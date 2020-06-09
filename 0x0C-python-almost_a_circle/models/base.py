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
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries):
            listd = {}
            return listd
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__ + ".json", "a", encoding="utf-8") as f:
            f.write(Base.to_json_string(list_objs))
            print(list_objs)
