#!/usr/bin/python3
"""
Module 9-rectangle

Defines Class Rectangle that inherits from BaseGeometry class

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines class Rectangle

    Methods:
        __init__()
        area()
        __str__()
    """
    def __init__(self, width, height):
        """
        Initializes the rectangle class

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Claculates the area of the rectangle

        Args:
            none
        Returns:
            Area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns:
            The string representation of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
