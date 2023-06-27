#!/usr/bin/python3
"""
Module 102-square
Defines class Square with private size and public area
Can access and update size
"""


class Square:
    """
    class Square definition

    """

    def __init__(self, size=0):
        """
        Initializes square

        Attributes:
            size (int): size of the square sides. Throw an error if size
                is not an int or is less than 0
        """
        self.size = size

    @property
    def size(self):
        """"
        Getter method

        Returns: self.__size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to update value of __size field

        Args:
            value (int): update square size only if it is an int and
                it is greater than 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates area of square
        Returns:
            area
        """
        return (self.__size)**2

    def __eq__(self, other):
        """
        Compares and returns if equal
        """
        if type(other) == Square:
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Compares and returns if not equal
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Compares and returns if lesser than
        """
        if type(other) == Square:
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Compares and returns if lesser than or equal to
        """
        if type(other) == Square:
            return self.area() <= other.area()
        return False

    def __gt__(self, other):
        """
        Compares and returns if greater than
        """
        if type(other) == Square:
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Compares and returns if greater than or equal to
        """
        if type(other) == Square:
            return self.area() >= other.area()
        return False
