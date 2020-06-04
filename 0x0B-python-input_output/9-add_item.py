#!/usr/bin/python3
""" Load, add, save """

from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    item = load_from_json_file("add_item.json")
except FileNotFoundError:
    item = []
item.extend(argv[1:len(argv)])
save_to_json_file(item, "add_item.json")
