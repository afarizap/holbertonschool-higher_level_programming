#!/usr/bin/python3
"""
print complete name
"""


def say_my_name(first_name, last_name=""):
    """ print first and last name in formated string """

    err1 = "first_name must be a string"
    err2 = "last_name must be a string"
    err3 = "TypeError: say_my_name() missing 1 required \
    positional argument: 'first_name'"
    if type(first_name) is not str:
        raise TypeError(err1)
    if type(last_name) is not str:
        raise TypeError(err2)
    if not first_name:
        raise TypeError(err3)
    print("My name is {} {}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest

    doctest.testfile("./tests/3-say_my_name.txt")
