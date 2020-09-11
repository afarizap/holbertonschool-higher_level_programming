#!/bin/bash/python3
def complex_delete(a_dictionary, value):
    new = a_dictionary
    for keys, values in list(new.items()):
        if values == value:
            new.pop(keys)
    return new
