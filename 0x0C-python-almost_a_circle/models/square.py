#!/usr/bin/python3
"""Module for square class representation."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square definition."""

    def __init__(self, size, x=0, y=0, id=None):
        """Square initialisation method.

        Args:
            size (int): the size of the square
            x (int): the x coordonate of the square
            y (int): the y coordonate of the square
            id (int): the id of the square instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String method of the square.
        Format: [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter method for the size property of the square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def update(self, *args, **kwargs):
        """Update method for the properties of the square.

        Args:
            args: list of variable length of no-keyworded arguments
            kwargs: variable length of keyworded arguments
        """
        attrs = ["id", "size", "x", "y"]
        if len(args) != 0:
            for key, value in enumerate(args):
                if key < 4:
                    setattr(self, attrs[key], value)
                else:
                    break
        else:
            for key, value in kwargs.items():
                if hasattr(self,key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary represention of a square."""
        square_dict = {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

        return square_dict
