#!/usr/bin/python3
""" takes in a URL, sends a request and displays the value of
X-Request-Id in the response header
"""
import requests
from sys import argv


if __name__ == '__main__':
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
