#!/usr/bin/python3
""" return if the object is an instance of a class that inherited
directly or indirectly from the specified class """


def inherits_from(obj, a_class):
    """ return true or false """
    if type(obj) is a_class:
        return False
    return issubclass(obj.__class__, a_class)
