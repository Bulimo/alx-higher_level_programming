#!/usr/bin/python3
"""
Module 3-sqare:
    defines a square class
"""


class Square:
    """
    A class Square definition
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

    def area(self):
        """
        Method to calculate the area of the current square

        Takes no arguments but uses the __size field
        """
        return self.__size * self.__size
