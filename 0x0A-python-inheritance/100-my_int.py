#!/usr/bin/python3
"""
Module 100-my_int

Defines Class MyInt with cint as base class
"""


class MyInt(int):
    """
    Class with inverted equality operatores '==' and '!='

    Methods:
        __eq__()
        __ne__()
    """

    def __eq__(self, other):
        """
        eqality operator:
        Args:
            other(int): object to check equality

        Returns:
            True if not equal and false if equal
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        ineqality operator:
        Args:
            other(int): object to check equality

        Returns:
            True if equal and false if not equal
        """
        return super().__eq__(other)
