#!/usr/bin/python3
""" takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': ''}

    if sys.argv[1]:
        data['q'] = sys.argv[1]

    r = requests.post(url, data)
    if r.get(data[q]):
        try:
            valid = json.loads(r)
            print('[{}] {}'.format(r.get('id'), r.get('name')))
        except:
            print('Not a valid JSON')
    else:
        print('No result')
