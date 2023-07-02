#!/usr/bin/python3
"""
Module 0-add_integer:
    contains an implementation of add_integer() function
    Functions: add_integer: returns sum of two integers passed as arguments
"""


def add_integer(a, b=98):
    """
    Function to add two integers passed as arguments

    Args:
        a(int): first number to be added
        b(int): second number to be added

    Returns: a + b
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return int(a + b)
