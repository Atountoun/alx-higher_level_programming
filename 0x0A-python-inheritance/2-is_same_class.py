#!/usr/bin/python3
"""A module for a checker function."""


def is_same_class(obj, a_class):
    """Tests if an object is exactly an instance of the
    specified class.

    Return:
        True: if that is the case
        False: if not
    """
    return type(obj) == a_class
