#!/usr/bin/python3
"""
Module base

Defines Class Base
"""

import json
import csv
import os


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
            return "[]"
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list_objs in CSV format and saves it to a file.

        Args:
            list_objs (list): List of instances to serialize
        """

        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline="") as my_file:
            writer = csv.writer(my_file)
            if list_objs is not None:
                writer.writerow(list_objs[0].to_dictionary().keys())
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary().values())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize CSV format file and create Instance objects.

        Returns:
            list: List of instances
        """
        filename = "{}.csv".format(cls.__name__)
        instances = []
        if os.path.exists(filename):
            with open(filename, "r", newline="") as my_file:
                reader = csv.reader(my_file)
                next(reader, None)
                for row in reader:
                    row = [int(value) for value in row]
                    if cls.__name__ == "Rectangle":
                        obj = cls(*row[1:])
                    elif cls.__name__ == "Square":
                        obj = cls(row[1])
                    obj.id = row[0]
                    instances.append(obj)
        return instances
