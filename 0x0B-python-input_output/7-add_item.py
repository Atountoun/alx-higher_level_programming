#!/usr/bin/python3
"""
A module that defines a function for saving and loading data
using file.
"""
import sys
import json
from os import path
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
new_data = sys.argv[1:]

if not path.exists(filename):
    save(new_data, filename)
else:
    data = load(filename)
    data.extend(new_data)
    save(data, filename)
