#!/usr/bin/python3
"""A module that defines a function for manipulating json."""
import json


def from_json_string(my_str):
    """Function for converting a json string to python data structure
    object

    Args:
        my_str (str): the json string to converted

    Return:
        A python data structure for the json string
    """
    return json.loads(my_str)
