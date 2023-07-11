#!/usr/bin/python3
import json
"""
Module 3-to_json_string

Functions:
    to_json_string()
"""


def to_json_string(my_obj):
    """
    Changes an object to JSON string representation

    Args:
        Object to print JSON repreentation

    Returns:
        the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
