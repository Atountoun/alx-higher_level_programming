#!/usr/bin/python3
"""This module contains a single function for addition."""


def add_integer(a, b=98):
    """Add two numbers a and b(by default = 98)

    Args:
        a (int, float): the first parameter
        b (int, float): the second parameter, by defaul 98

    Returns:
        The result of a + b
    """
    types = (int, float)
    if not isinstance(a, types):
        raise TypeError("a must be an integer")
    elif not isinstance(b, types):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
