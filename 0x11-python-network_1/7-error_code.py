#!/usr/bin/python3
""" takes in a URL, sends a request and displays the body
"""
import requests
import sys


if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    if r.code >= 400:
        print('Error code: {}'.format(r.code))
    else:
        print(r.text)
