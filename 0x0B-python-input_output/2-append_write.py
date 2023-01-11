#!/usr/bin/python3
"""A module that defines a function for appending a string
at the end of a text file.
"""


def append_write(filename="", text=""):
    """This function appends a string at the end of a text line
    and returns the number of characters added.

    Args:
        filename (str): the name of the file to use
        text (str): the text to be appended to the file
    """
    chars = 0
    with open(filename, "a") as f:
        chars = f.write(text)

    return chars
