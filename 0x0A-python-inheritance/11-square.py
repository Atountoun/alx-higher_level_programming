#!/usr/bin/python3
"""A module that defines an inherited class from Rectangle
called Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """The square instantiation method:

        Args:
            size (int): the size of the side of the square
        """
        super().__init__(size, size)

    def area(self):
        """Reimplementation of the area method for the square

        Return:
            size * size : the area formula of a square
        """
        return super().area()

    def __str__(self):
        """Returns the square description: [Square] <width>/<height>"""
        return super().__str__()

    def print(self):
        """Prints the square description: [Square] <width>/<height>"""
        super().print()
