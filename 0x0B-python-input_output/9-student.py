#!/usr/bin/python3
"""
Module 9-student

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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
