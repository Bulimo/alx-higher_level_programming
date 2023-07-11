#!/usr/bin/python3
"""
Module 2-append_write

Functions:
    append_write()
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file

    Args:
        filename: text file to append to
        text(str): string to append to the file

    Returns:
        Number of characters appended
    """
    with open(filename, mode="a", encoding="utf-8") as my_file:
        count = my_file.write(text)

    return count
