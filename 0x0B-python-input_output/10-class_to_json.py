#!/usr/bin/python3
""" Class to JSON """


def class_to_json(obj):
    """ returns the dictionary description for JSON """
    return obj.__dict__
