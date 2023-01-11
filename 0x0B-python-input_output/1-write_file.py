#!/usr/bin/python3
"""A module that defines a fuction for writing a string
to a text file(utf8).
"""


def write_file(filename="", text=""):
    """Writes a string to a text file(utf8).

    Args:
        filename (str): the name of the file
        text (str): the string text to write into the file
    """
    chars = 0
    with open(filename, "w") as f:
        chars = f.write(text)

    return chars
