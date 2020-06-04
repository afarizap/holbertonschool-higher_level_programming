#!/usr/bin/python3
""" read file method """


def read_file(filename=""):
    """ read a text file UTF-8 and print stdout """
    with open(filename, "r", encoding="utf-8") as f:
        readf = f.read()
        print(readf, end="")
