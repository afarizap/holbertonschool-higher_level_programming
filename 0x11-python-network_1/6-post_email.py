#!/usr/bin/python3
""" Takes in a URL and an email address, sends a POST request with the email
 as a parameter, and finally displays the body.
"""
from request import post
from sys import argv


if __name__ == '__main__':
    r = post(argv[1], {'email': argv[2]})
    print(r.text)
