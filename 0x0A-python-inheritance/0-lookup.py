#!/usr/bin/python3
"""
Module 0-lookup : defines function to print the attributes of an object

"""


def lookup(obj):
    """
    Arguments:
        obj: any type. Object to get its attributes
    Return:
        List of attributes found
    """
    return dir(obj)
