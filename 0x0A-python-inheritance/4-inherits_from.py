#!/usr/bin/python3
"""A module that check for inheritance"""


def inherits_from(obj, a_class):
    """Checks if an object inherits from a given class

    Args:
        obj: the object to check
        a_class: the class to be used

    Return:
        True: if obj inherits from a_class
        Fale: if obj does not inherit from a_class
    """
    return issubclass(type(obj), a_class)
