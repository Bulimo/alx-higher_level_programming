#!/usr/bin/python3
"""
Module 1-rectangle
Defines a rectangle class
"""


class Rectangle:
    """
    Class Rectangle definition

    Methods:
        __init__(): creates an object instance
        width(): width attribute getter and setter methods
        height(): height attribute getter and setter methods
    """
    def __init__(self, width=0, height=0):
        """
        Method to initialize an instance of Rectangle object

        Args:
            width(int): width size of the rectangle
            height(int): height size of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Getter method to retrieve the width of the current Rectangle

        Return:
            width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method to update the width attribute

        Args:
            value(int): size of the width of Rectangle
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method to retrieve the height of the current Rectangle

        Return:
            height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method to update the height attribute

        Args:
            value(int): size of the height of Rectangle
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
