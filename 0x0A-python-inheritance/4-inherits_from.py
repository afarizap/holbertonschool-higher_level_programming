#!/usr/bin/python3
""" return if the object is an instance of a class that inherited
directly or indirectly from the specified class """


def inherits_from(obj, a_class):
    """ return true or false """
    return issubclass(obj, a_class)
