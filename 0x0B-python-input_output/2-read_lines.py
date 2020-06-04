#!/usr/bin/python3
""" Read n lines """


def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text UTF-8 and prints into stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for line in range(nb_lines):
                print(f.readline(), end="")
