#!/bin/bash/python3
def complex_delete(a_dictionary, value):
    for keys, values in list(a_dictionary.items()):
        if values == value:
            a_dictionary.pop(keys)
    return a_dictionary
