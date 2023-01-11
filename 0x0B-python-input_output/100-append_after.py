#!/usr/bin/python3
"""A module tht defines a function for manipulation files."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing
    a specific string.

    Args:
        filename (str): the name of the file
        search_string (str): the specific string to look for
        new_string (str): the new string to insert to the file
    """
    with open(filename, "r+") as f:
        lines = f.readlines()
        if search_string in lines[-1]:
            lines.append(new_string)
        for key, line in enumerate(lines):
            if search_string in line:
                lines.insert(key + 1, new_string)
        f.seek(0)
        f.writelines(lines)
