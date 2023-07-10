#!/usr/bin/python3
"""
Module 8-rectangle

Defines Class Rectangle that inherits from BaseGeometry class

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines class Rectangle

    Methods:
        __init__()
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
