#!/usr/bin/python3
""" Class that prevents creating new instances, except for "first_name"""


class LockedClass:
    """ this has no atributes """
    __slots__ = 'first_name'
