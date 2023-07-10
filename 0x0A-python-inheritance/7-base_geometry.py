#!/usr/bin/python3
"""
Module 7-base_geometry

Defines class BaseGeometry

Methods:
    area()
    integer_validator()
"""


class BaseGeometry:
    """
    Methods:
        area()
        integer_validator()
    """
    def area(self):
        """
        Raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the input value argument

        Args:
            name(string): name
            value(int): value provided and to be validated

        Raises an error if value fails
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
