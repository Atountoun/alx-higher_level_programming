#!/usr/bin/python3
"""A simple module with one function named say_my_name."""


def say_my_name(first_name, last_name=""):
    """This function prints My name is
    <first name> <last name>

    Args:
        first_name (str): the first name
        last_name (str): the last name

    Raises:
        TypeError:
            If first_name and last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {first} {last}".format(first=first_name, last=last_name))
