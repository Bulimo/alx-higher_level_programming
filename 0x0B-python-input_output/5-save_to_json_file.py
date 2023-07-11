#!/usr/bin/python3
"""
Module 5-save_to_json_file

Functions:
    save_to_json_file()
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to testfile usig JSON representation

    Args:
        my_obj: object to write to text file
        filename: text file to write to

    Returns:
        None
    """
    import json
    # json_obj = json.dumps(my_obj)

    with open(filename, mode="w", encoding="utf-8") as my_file:
        # json_obj = json.dumps(my_obj)
        # my_file.write(json_obj)
        json.dump(my_obj, my_file)
