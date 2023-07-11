#!/usr/bin/python3
"""
Module 6-load_from_json_file

Functions:
    load_from_json_file()
"""


def load_from_json_file(filename):
    """
    creates an Object from a JSON file

    Args:
        filename(.json). JSON file to create a Python Object from

    Returns:
        Created Python Object
    """
    import json
    with open(filename, encoding="utf-8") as my_file:
        return json.load(my_file)
