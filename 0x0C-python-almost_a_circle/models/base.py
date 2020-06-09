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
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        jlist = []
        if len(list_objs) is 0:
            pass
        else:
            for obj in list_objs:
                jlist.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(jlist))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) is 0:
            return []
        else:
            return json.loads(json_string)
