#!/usr/bin/python3
"""A module that defines a class Student."""


class Student:
    """Class for representing a student."""

    def __init__(self, first_name, last_name, age):
        """The class initialization method.

        Args:
            first_name (str): the first name of the student
            last_name (str): the last name of the student
            age (int): the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """The method that retrieves a dictionary representation
        of a Student instance
        """
        result = dict()
        if attrs is None:
            return self.__dict__
        for attr in attrs:
            if attr in self.__dict__.keys():
                result[attr] = self.__dict__[attr]
        return result
