#!/usr/bin/python3
"""
Module 0-read_file

Functions:
    read_file()
"""


def read_file(filename=""):
    """
    Reads a text file and prints to stdout

    Args:
        filename: text file to read

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as my_file:
        for line in my_file:
            print(line, end="")
