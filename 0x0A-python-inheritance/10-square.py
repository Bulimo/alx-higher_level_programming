#!/usr/bin/python3
"""
Module 10-square

Defines Class Square that inherits from Rectangle class

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines class Square

    Methods:
        __init__()
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
