#!/usr/bin/python3
"""
Module 3-say_my_name: contains implementation of say_may_name()

Functions:
    say_my_name: function that prints out user's name passed as argument
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints out first and last name passed as arguments

    Args:
        first_name(string): first name of user's full name
        last_name(string): last name of user's full name
    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')

    if type(last_name) != str:
        raise TypeError('last_name must be a string')

    print("My name is {:s} {:s}".format(first_name, last_name))
