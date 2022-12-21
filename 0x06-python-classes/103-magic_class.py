#!/usr/bin/python3
"""Define module for the python bytecode given."""


class MagicClass:
    """Class that represents the assembly of the Python bytecode."""

    def __init__(self, radius=0):
        """The magic class constructor

        Args:
            radius (int or float): the radius of the MagicClass
        """
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """The method to calculate the area of the MagicClass"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """The method to calculate the circumference of the MagicClass"""
        return (2 * math.pi * self.__radius)
