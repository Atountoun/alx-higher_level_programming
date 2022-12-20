#!/usr/bin/python3
class Square:
    """A class that defines a square object."""
    def __init__(self, size=0):
        """The Square constructor method.
        Args:
            size: the size of the square with default value as 0.
        """
        self.size = size

    @property
    def size(self):
        """The size getter method as property of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """The size setter method as property of the square
        Args:
            value: the value to be set to the size of the square
        """
        try:
            self.__size = int(value)
            if value < 0:
                raise ValueError("size must be >= 0")
        except Exception:
            raise TypeError("size must be an integer")

    def area(self):
        """The area of a square method.
        Args:
            No args
        Returns:
            The area of the square
        """
        return self.__size * self.__size
