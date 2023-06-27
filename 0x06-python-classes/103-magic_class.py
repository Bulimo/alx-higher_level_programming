#!/usr/bin/python3
"""Define MagicClass"""
import math


class MagicClass:
    """
    Initialize an instance of magic class
    Define methods area and circumference
    """
    def __init__(self, radius=0):
        """
        Initialize MagicClass object
        Attributes:
            radius: radius of the class
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calcualte circumference"""
        return 2 * math.pi * self.__radius
