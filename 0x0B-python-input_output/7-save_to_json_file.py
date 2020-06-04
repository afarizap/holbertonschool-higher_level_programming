#!/usr/bin/python3
""" Save object to a file """


def save_to_json_file(my_obj, filename):
    """ writes an object to a text file, using a JSON rep """
    import json
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
