#!/usr/bin/python3
"""
Module 1-my_list
"""


class MyList(list):
    """
    Inherits from list class
    """
    def print_sorted(self):
        """
        prints a sorted list
        """

        print(sorted(self))
