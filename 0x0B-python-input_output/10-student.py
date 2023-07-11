#!/usr/bin/python3
"""
Module 10-student

Class:
    Student
"""


class Student:
    """
    Defines class Stident

    Attributes:
        first_name
        last_name
        age

    Methods:
        __init__(self)
        to_json(self)
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes Student instance object

        Args:
            first_name(str): first name
            last_name(str): last name
            age: age of the student

        Returns:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Args:
            attrs(list): list of strings of attributes to be retrieved

        Returns:
            dictioanry of retrieved attributes
        """
        if attrs is None or len(attrs) == 0:
            return self.__dict__
        ds = self.__dict__
        return {k: ds[k] for k in attrs & ds.keys()}
