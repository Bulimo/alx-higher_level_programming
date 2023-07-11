#!/usr/bin/python3
"""
Module 7-add_item

Functions:
    load_from_json_file()
    save_to_json_file()
"""


def add_item(files):
    """
    adds all arguments to a Python list, and then save them to a file

    Returns:
        None
    """
    save_to_json = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = __import__('6-load_from_json_file').load_from_json_file

    my_file = "add_item.json"

    try:
        ls = load_from_json(my_file)
    except Exception:
        ls = []
    ls += files
    save_to_json(ls, my_file)


if __name__ == '__main__':
    """
    Calls the function to add item when called
    """
    import sys

    files = sys.argv[1:]
    add_item(files)
