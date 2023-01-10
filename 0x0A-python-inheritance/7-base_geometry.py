#!/usr/bin/python3
"""A module that defines a class named BaseGeometry."""


class BaseGeometry:
    """The base class use for geometry."""

    def area(self):
        """Raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the argument named value passed.

        Args:
            name (string): the name of the property
            value (int): the value associate to the property

        Raise:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
