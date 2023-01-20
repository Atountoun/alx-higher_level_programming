#!/usr/bin/python3
"""The module of the base class of all other class in this project."""
import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert the list of dictionaries to json.

        Args:
            list_dictionaries (list of dict): a list of dictionaries

        Return:
            the json string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return []

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the json string representation of list_objs to a file.

        Args:
            list_objs ([]): list of instances who inherits of Base.

        Required:
            filename: <Class name>.json
        """
        data = []
        filename = ""
        if list_objs is None:
            data = []
        else:
            filename = str(list_objs[0].__class__.__name__) + ".json"
            data = json.loads(cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]
                    ))
            with open(filename, "w") as fd:
                json.dump(data, fd)

    @staticmethod
    def from_json_string(json_string):
        """Static method used for json convertion to python data object

        Args:
            json_string (string): a string representing a list of dictionaries

        Return:
            the list of the json string representation json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This method is used to create a new instance of the Base class.

        Args:
            dictionary (dict): a keyworded argument with attributes.

        Return:
            An instance with all attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                instance = cls(5, 7)
            else:
                instance = cls(4)
            instance.update(**dictionary)
            return instance

    @classmethod
    def load_from_file(cls):
        """This method is used to retrives instances saved in a json file.

        Return:
            An empty list if the file doesn't exist
            Else, the list of the instances
        """
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename) as fd:
                dicts = Base.from_json_string(fd.read())
                ls = [cls.create(**d) for d in dicts]
                return ls
        else:
            return []
