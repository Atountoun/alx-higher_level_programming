#!/usr/bin/python3
"""A module that defines a single function."""


def is_kind_of_class(obj, a_class):
    """Tests if an object is an instance of, or if an object
    is an instance of a class that inherited from the specified class.

    Return:
        True: if obj is instance of class or of class inherited from class
        False: if not
    """
    return isinstance(obj, a_class)
