#!/usr/bin/python3
"""module of json file function"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

open("add_item.json", "a")

try:
    arr = load_from_json_file("add_item.json")
except ValueError:
    arr = []

save_to_json_file(arr + sys.argv[1:], "add_item.json")
