#!/usr/bin/python3
"""The module for class Rectangle that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """The representation of a class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The constructor method of the rectangle class.

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): the x coordinate
            y (int): the y coordinate

        Raise:
            TypeError: if a given attribute is not an integer
            ValueError: if width or height are under 0 or equals to 0
                        if x or y are under 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle.

        Return:
            width * height
        """
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle with the # character."""
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Prints the rectangle with a specific format:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - " \
               f"{self.__width}/{self.__height}"

    def update(self, *args):
        """Update the rectangle with the argmments passed to the method.

        Args:
            args : no-keywords arguments with variable length
        """
        self.__x = args[0] if args[0] else self.__x
        self.__y = args[1] if args[1] else self.__y
        self.__width = args[2] if args[2] else self.__width
        self.__height = args[3] if args[3] else self.__height
        self.id = args[4] if args[4] else self.id
