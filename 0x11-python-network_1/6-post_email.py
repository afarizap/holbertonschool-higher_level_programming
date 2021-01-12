#!/usr/bin/python3
""" Takes in a URL and an email address, sends a POST request with the email
 as a parameter, and finally displays the body.
"""
import requests
import sys


if __name__ == '__main__':
    r = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(r.text)
