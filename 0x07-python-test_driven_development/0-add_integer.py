#!/usr/bin/python3

""" add integer funciton """

def add_integer(a, b=98):

    """ adds two integers a and b """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(a) is float:
        a = int(a)
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    elif type(b) is float:
        b = int(b)

    return a + b
