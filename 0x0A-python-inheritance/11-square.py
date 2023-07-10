#!/usr/bin/python3
"""
Module 11-square

Defines Class Square with Rectangle class as base

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines class Square

    Methods:
        __init__()
        __str__()
    """
    def __init__(self, size):
        """
        Initializes the rectangle class

        Args:
            size(int): size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Claculates the area of the square

        Args:
            none
        Returns:
            Area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns:
            The string representation of the Squre
        """
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)
