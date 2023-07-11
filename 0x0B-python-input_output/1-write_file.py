#!/usr/bin/python3
"""
Module 1-write_to_file

Functions:
    write_file()
"""


def write_file(filename="", text=""):
    """
    Function that writes to text file

    Args:
        filename: the file to write to
        text(str): the content to write

    Returns:
        number of characters written
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        count = my_file.write(text)

    return count
