#!/usr/bin/python3
""" To JSON string """


def to_json_string(my_obj):
    """ returns the JSON representaiton of an object (sstring) """
    import json
    return json.dumps(my_obj)
