#!/usr/bin/python3
""" Number of lines """


def number_of_lines(filename=""):
    """ returns the number of lines of a text file """
    with open(filename, "r", encoding="utf-8") as f:
        lines = len(f.readlines())
    return lines
