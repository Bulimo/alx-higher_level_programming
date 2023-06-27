#!/usr/bin/python3
"""
Module 2-sqare:
    defines a square class
"""


class Square:
    """
    A class Square definition
    Square with private attribute size
    """
    def __init__(self, size=0):
        """
        Initializes an instance of Square object

        Args:
            size(int): size of the side of the square
                Throw an error if size is not an int or if < 0
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
