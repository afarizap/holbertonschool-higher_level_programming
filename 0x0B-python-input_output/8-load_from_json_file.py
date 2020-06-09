#!/usr/bin/python3
""" Create object from a JSON file """


def load_from_json_file(filename):
    """ creates an object from a "JSON file" """
    import json
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)