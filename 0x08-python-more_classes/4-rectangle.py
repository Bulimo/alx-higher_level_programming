#!/usr/bin/python3
"""
Module 4-rectangle
Defines a rectangle class
"""


class Rectangle:
    """
    Class Rectangle definition

    Methods:
        __init__: creates an object instance
        width(): width attribute getter and setter method
        height(): height attribute getter and setter method
        area(): returns the area of the rectangle
        perimeter(): returns perimeter of the rectangle
        __str__(): returns a string of the rectangle with characters #
        __repr__(): returns a string representation of the rectangle
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

    def area(self):
        """
        method that claculates and returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        method that claculates and returns the perieter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        method that returns a string of the Rectangle printed wit characters
        '#'
        """
        res_str = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                res_str += "#" * self.__width
                if i + 1 != self.__height:
                    res_str += "\n"

        return res_str

    def __repr__(self):
        """
        Method that returns a string representation of the Rectangle object.
        Allows for an object to be recreated from the string returned
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
