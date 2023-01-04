#!/usr/bin/python3
"""Module that defines a Rectangle class."""


class Rectangle:
    """Class Rectangle that defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """The constructor of the class.

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Use to get the value of the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Use to get the value of the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.__height) * 2

    def __str__(self):
        """Prints the rectangle with the character #."""
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = []
        for i in range(self.__height):
            line = ""
            for j in range(self.__width):
                line += str(self.print_symbol)
            lines.append("".join(line))

        return '\n'.join(lines)

    def __repr__(self):
        """Returns the representation of the class."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """The instance deletion magic method."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
