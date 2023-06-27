#!/usr/bin/python3
"""
Module 6-sqare:
    defines a square class
"""


class Square:
    """
    A class Square definition

    Args:
        size (int): size of a side in square
        position (int): position of the square

    Functions:
        __init__(self, size, position)
        size(self)
        size(self, value)
        position(self)
        position(self, value)
        area(self)
        my_print(self)
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes an instance of Square object

        Args:
            size(int): size of the side of the square
                Throw an error if size is not an int or if < 0
            position (int): tuple of two positive integers
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Method to calculate the area of the current square

        Return:
            self.__size * self.__size
        """
        return self.__size ** 2

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
        Setter method to update the value of the size field

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

    @property
    def position(self):
        """
        Getter method to retrieve the positon of the current square

        Return:
            self.__position field
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to update the value of the position field

        Args:
            value(tuple): position of the square
                Throw an error if position is not a tuple of 2 integers
        """
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int \
                or type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """
        Method that prints in stdout the square with the character #
        """
        if (self.__size == 0):
            print("")
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
