#!/usr/bin/python3
"""
This is the add_integer module
it returns the addition of two integers
if a float is given its converted to int
"""


def add_integer(a, b=98):
    """
    This is the add integer function
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")
