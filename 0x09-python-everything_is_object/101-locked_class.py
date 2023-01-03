#!/usr/bin/python3
"""Module that defines a class with restrictions."""


class LockedClass:
    """LockedClass used to prevent creation of some attributes."""
    def __setattr__(self, attr, value):
        """The magic method called when setting attribute for an object."""
        if attr == "first_name":
            self.__dict__[attr] = value
            return

        raise AttributeError(f"'LockedClass' object has no attribute '{attr}'")
