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

    def area(self):
        """Implementation of the area method herited from BaseGeometry.

        Return:
            width * height: the area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Dunder method for str

        Return:
            [Rectangle] <width>/<height>
        """
        return "[{}] <{}>/<{}>".format(self.__class__.__name__, self.__width, self.__height)

    def print(self):
        """Prints [Rectangle] <width>/<height>"""
        print(self)
