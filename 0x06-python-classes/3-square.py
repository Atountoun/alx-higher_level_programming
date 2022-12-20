#!/usr/bin/python3
class Square:
    """A class that defines a square object."""
    def __init__(self, size=0):
        """The Square constructor method.
        Args:
            size: the size of the square with default value as 0.
        """
        try:
            self.__size = int(size)
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")

    def area(self):
        """The area of a square method.
        Args:
            No args
        Returns:
            The area of the square
        """
        return self.__size * self.__size
