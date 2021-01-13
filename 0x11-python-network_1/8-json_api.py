#!/usr/bin/python3
""" takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) == 1:
        q = ''
    else:
        q = sys.argv[1]

    r = requests.post(url, data={'q': q})

    if r.json():
        print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
    else:
        print("No result")
