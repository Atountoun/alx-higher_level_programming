#!/usr/bin/python3
"""A module that defines a modified class of int."""


class MyInt(int):
    """MyInt inherits from int."""

    def __eq__(self, other):
        """
        Redifines the built-in function equal by changing it
        to not equal

        Args:
            other (int): the value to compare

        Return:
            True: if the two numbers are not equal
            False: if they are equal
        """
        return self is other

    def __ne__(self, other):
        """
        Redifines the built-in function not equal by changing it
        to not equal

        Args:
            other (int): the value to compare

        Return:
            True: if the both values are equal
            False: if they are not equal
        """
        return self is not other
