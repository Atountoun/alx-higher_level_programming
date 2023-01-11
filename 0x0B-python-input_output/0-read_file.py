#!/usr/bin/python3
"""A module that defines a function for reading text file(UTF8)"""


def read_file(filename=""):
    """Reads a text file(utf-8) and prints it to stdout.

    Args:
        filename (str): the name of the file to read
    """
    with open(filename, "r", "utf-8") as f:
        for line in f:
            print(line)
