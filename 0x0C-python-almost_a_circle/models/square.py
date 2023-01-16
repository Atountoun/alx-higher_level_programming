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
