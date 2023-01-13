#!/usr/bin/python3
"""The module of the base class of all other class in this project."""


class Base:
    """The base class of all others."""
    __nb_objects = 0

    def __init__(self, id=None):
        """The constructor of the class Base

        Args:
            id (int): the instance identifier
        """
        if not id:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        else:
            self.id = id
