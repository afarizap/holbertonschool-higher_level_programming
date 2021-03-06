#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request with the email
 as a parameter, and displays the body of the response decoded in utf-8
"""
from urllib import request, parse
from sys import argv


if __name__ == '__main__':
    data = parse.urlencode({'email': argv[2]})
    data = data.encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
