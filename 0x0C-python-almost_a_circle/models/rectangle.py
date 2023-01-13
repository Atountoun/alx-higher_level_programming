#!/usr/bin/python3
"""The module for class Rectangle that inherits from Base."""
Base = __import__('base').Base


class Rectangle(Base):
    """The representation of a class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The constructor method of the rectangle class.

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): the x coordinate
            y (int): the y coordinate
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = x

    @property
    def width(self):
        """The getter method of the width property of a rectangle."""
        return self.__width

    @property
    def height(self):
        """The getter method of the height property of a rectangle."""
        return self.__height

    @property
    def x(self):
        """The getter method of the x property of a rectagle."""
        return self.__x

    @property
    def y(self):
        """The getter method of the y property of a rectangle."""
        return self.__y

    @width.setter
    def width(self, width):
        self.__width = width

    @height.setter
    def height(self, height):
        self.__height = height

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y
