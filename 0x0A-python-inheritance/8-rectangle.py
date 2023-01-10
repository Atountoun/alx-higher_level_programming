#!/usr/bin/python3
"""A module that defines a class named Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """The class constructor method.

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
