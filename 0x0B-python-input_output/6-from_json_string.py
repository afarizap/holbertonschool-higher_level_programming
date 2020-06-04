#!/usr/bin/python3
""" From JSON string to Object """


def from_json_string(my_str):
    """ return an object (python) represented by json string """
    import json
    return json.loads(my_str)
