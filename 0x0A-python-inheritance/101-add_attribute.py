#!/usr/bin/python3
"""A module with a function to add a new attribute to an object."""


def add_attribute(obj, name, value):
    """Funtion that adds a new attribute to an object if it's possible.

    Args:
        obj: the object to which the attribute will be added
        name (str): the name of the attribute
        value: the value to be set to the attribute

    Raise:
        TypeError: if the object can't have new attribute
    """
    if hasattr(obj, name) or not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
