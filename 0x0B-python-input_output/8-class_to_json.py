#!/usr/bin/python3
"""A module for converting class to json."""


def class_to_json(obj):
    """Function that returns the dictionary description
    with simple data structure for json serialization

    Args:
        obj (instance of class): the object to be used

    Return:
        The dictionary description with simple data structure
    """
    return obj.__dict__
