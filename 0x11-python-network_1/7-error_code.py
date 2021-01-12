#!/usr/bin/python3
""" takes in a URL, sends a request and displays the body
"""
from request import get
from sys import argv


if __name__ == '__main__':
    r = get(argv[1], {'email': argv[2]})
    if r.code >= 400:
        print('Error code: {}'.format(r.code))
    else:
        print(r.text)
