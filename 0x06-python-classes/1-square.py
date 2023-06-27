#!/usr/bin/python3
"""
Module 1-sqare:
    defines a square class
"""


class Square:
    """
    A class Square definition
    Square with private attribute size
    """
    def __init__(self, size):
        """
        Initializes an instance of Square object

        Args:
            size: size of the side of the square
        """
        self.__size = size
