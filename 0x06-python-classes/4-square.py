#!/usr/bin/python3
"""
Module -sqare:
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
        self.__size = size

    def area(self):
        """
        Method to calculate the area of the current square

        Return:
            self.__size * self.__size
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the current square

        Return:
            self.__size field
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to update the value of the __size field

        Args:
            value(int): size of the side of the square
                Throw an error if size is not an int or if < 0
        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
