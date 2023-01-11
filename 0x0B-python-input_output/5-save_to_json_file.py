#!/usr/bin/python3
"""A module that defines a function for writing json to a file."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a json representation.

    Args:
        my_obj (str): the object to write to the text file
        filename (str): the file to be used
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
