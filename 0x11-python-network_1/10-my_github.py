#!/usr/bin/python3
""" takes your Github credentials (username and password) and uses the
 Github API to display your id 54fbeabdbf85074d97245300a7f4007991143ba9
"""
import requests
import sys


if __name__ == '__main__':
    r = requests.get('https://api.github.com/user', auth=(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))
