#!/usr/bin/python3
"""
Module 100-append_after

Functions:
    append_after()
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing a specific
    string

    Args:
        filename: file to read
        search_string(str): string in filename to add new string after
        new_string(str): string to add after search_string is found

    Returns:
        None
    """
    with open(filename, mode="r", encoding="utf-8") as my_file:
        s = ""
        for line in my_file:
            s += line
            if search_string in line:
                s += new_string
    with open(filename, mode="w", encoding="utf-8") as my_file:
        my_file.write(s)
