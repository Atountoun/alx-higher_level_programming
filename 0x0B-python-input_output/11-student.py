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
        if not attrs:
            return self.__dict__
        for attr in attrs:
            result[attr] = self.__dict__[attr]
        return result

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): the dictionary contaning attributes
            as keys associated to new values.
        """
        for key, value in json.items():
            self.__dict__[key] = value
