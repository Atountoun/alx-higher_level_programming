#!/usr/bin/python3
"""Define a square class with a private instance attribute."""


class Square:
    """A class that defines a square object."""

    def __init__(self, size):
        """The square initialization method:

        Args:
            size (int): the size of the edge of the square.
        """
        self.__size = size
