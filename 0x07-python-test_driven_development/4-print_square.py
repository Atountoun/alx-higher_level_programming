#!/usr/bin/python3
"""A module that contains print_square function."""


def print_square(size):
    """The function prints a square with the character #.

    Args:
        size: the number of `#` to print as the square side

    Raises:
        ValueError:
            if size is less than 0
        TypeError:
            if size is not an integer
            if size is a float and is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
