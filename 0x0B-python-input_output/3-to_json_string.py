#!/usr/bin/python3
"""A module that defines a function for converting python object
to json one."""
import json


def to_json_string(my_obj):
    """Converts a python object to json object.

    Args:
        my_obj (str): the object to parse

    Return:
        The json representation of the object
    """
    return json.dumps(my_obj)
