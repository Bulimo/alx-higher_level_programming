#!/usr/bin/python3
"""
Module 9-rectangle
Defines a rectangle class
"""


class Rectangle:
    """
    Class Rectangle definition

    Attributes:
        number_of_instances: counts number of objects of Rectangle class
        print_symbol: symbol to use for string representation

    Methods:
        __init__: creates an object instance
        width(): width attribute getter and setter method
        height(): height attribute getter and setter method
        area(): returns the area of the rectangle
        perimeter(): returns perimeter of the rectangle
        __str__(): returns a string of the rectangle with characters #
        __repr__(): returns a string representation of the rectangle
        __del__(): prints a message when an instance of rectangle is deleted
        bigger_or_equal(): compares two rectangles with respect to area
        square(): returns new rectangle that is square
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Method to initialize an instance of Rectangle object

        Args:
            width(int): width size of the rectangle
            height(int): height size of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
                res_str += str(self.print_symbol) * self.__width
                if i + 1 != self.__height:
                    res_str += "\n"

        return res_str

    def __repr__(self):
        """
        Method that returns a string representation of the Rectangle object.
        Allows for an object to be recreated from the string returned
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Method to print a message when an instance of the Rectangle object is
        removed
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares to rectangles with respect to the area size

        Args:
            rect_1: first Rectangle instance to compare
            rect_2: second Rectangle instance to compare
        Return:
            Rectangle instance with the biggest area
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with width == height == size
        """
        return cls(size, size)
