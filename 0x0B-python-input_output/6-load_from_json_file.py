#!/usr/bin/python3
"""A module that defines a function for using data from json file."""
import json


def load_from_json_file(filename):
    """Creates an object from a json file.

    Args:
        filename (str): the file to be used
    """
    with open(filename, "utf-8") as f:
        data = json.load(f)

        return data
