#!/usr/bin/python3
""" manage id attribute, to avoid duplicating the same code """
import json
import os


class Base:
    """ first class base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ translate a dictionary to json string (dumps) """
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write json string in a file .json """

        jlist = []
        if list_objs is None:
            pass
        else:
            for obj in list_objs:
                jlist.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(jlist))

    @staticmethod
    def from_json_string(json_string):
        """ return json string LISTED """
        if json_string is None or len(json_string) is 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create a base instance """
        dummy = cls(1, 1, 1, 1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        with open(cls.__name__ + ".json", "r", "utf-8") as f:
            if 
            data = f.read
            data2 = cls.from_json_string(data)
