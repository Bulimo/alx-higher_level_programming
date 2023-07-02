#!/usr/bin/python3
"""
Module 4-print_square

Functions:
    print_square(): function that prints the square passed as an argument
"""


def print_square(size):
    """
    Function that prints a square with the character #

    Args:
        size(int): is the size length of the square
    """
    if type(size) == int:
        if size >= 0:
            for i in range(size):
                print("#" * size)
        else:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")
