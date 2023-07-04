#!/usr/bin/python3
"""
Module 101-locked_class
"""


class LockedClass():
    """
    Class definition that allows for anoly one attribute to be set dynamically
    """
    __slots__ = ['first_name']

    def __init__(self):
        """
        initialises an instance of the class object
        """
        self.first_name = 'name'
