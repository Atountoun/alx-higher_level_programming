#!/usr/bin/python3
"""Define a class square with instance attribute check."""


class Square:
    """A class that defines a square object and check the size attr."""

    def __init__(self, size=0):
        """The Square constructor method.

        Args:
            size (int): the size of the square with default value as 0.
        """
        try:
            self.__size = int(size)
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
