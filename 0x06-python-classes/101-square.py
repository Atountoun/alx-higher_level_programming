#!/usr/bin/python3
"""Class square module."""


class Square:
    """A class that defines a square object."""

    def __init__(self, size=0, position=(0, 0)):
        """The Square constructor method.

        Args:
            size: the size of the square with default value as 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """The size getter method as property of the square."""
        return self.__size

    @property
    def position(self):
        """The position method as property of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @size.setter
    def size(self, value):
        try:
            self.__size = int(value)
            if value < 0:
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

    def my_print(self):
        """A method used to print the square with the character #."""
        if self.__size == 0:
            print()
        else:
            [print() for i in range(self._position[1])]
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """Print representation of the Square."""
        lines = []
        if self.__size == 0:
            return ""
        [lines.append("") for i in range(self.__position[1])]
        for i in range(self.__size):
            line = ""
            for k in range(self.__position[0]):
                line += " "
            for j in range(self.__size):
                line += '#'
            lines.append(line)
        return ('\n'.join(lines))
