#!/usr/bin/python3
"""
Module base

Defines Class Base
"""

import json


class Base:
    """
    Definition of the Base class

    Attributes:
        __nb_objects

    Methods:
        __init__()
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Base class initializer

        Args:
            id(int): id of the object instance
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Generates JSON string representation of list_dictionaries

        Args:
            list_dictioanries: list of dictionaries

        Returns:
            Rreturns the JSON string representation of list_dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        <class name>.json

        Args:
            list_objs: list of instances that inherit from Base

        Returns:
            None
        """

        filename = cls.__name__ + ".json"
        if list_objs is not None:
            dict_list = [obj.to_dictionary() for obj in list_objs]
        else:
            dict_list = []

        jstring = cls.to_json_string(dict_list)
        with open(filename, "w") as my_file:
            my_file.write(jstring)

    @staticmethod
    def from_json_string(json_string):
        """
        Creates a Python Object from JSON string representation

        Args:
            json_string(str): string representing a list of dictionaries

        Returns:
            returns the list of the JSON string representation json_string
        """

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a Python Object from a dictioanry

        Args:
            dictioanry: dictionary of dictionaries of instances

        Returns:
            an instance with all attributes already set
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2)       # Create a rectangle instance

        if cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Creates a list of instances from a json file
        It employs the methods from_json_string and create

        Returns:
            A list of instances
        """

        filename = "{}.json".format(cls.__name__)
        instances = []
        try:
            with open(filename, mode="r", encoding="utf-8") as my_file:
                json_string = myfile.read()   # Read the JSON data

                # Change the JSON string into list of dictionaries
                dict_list = cls.from_json_string(json_string)

                for elem in dict_list:
                    instance = cls.create(**elem)
                    instances.append(instance)
        except Exception:
            return []

        return instances
