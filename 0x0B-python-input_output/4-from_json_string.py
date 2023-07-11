#!/usr/bin/python3
import json
"""
Module 4-from_json_string

Functions:
    from_json_string()
"""


def from_json_string(my_str):
    """
    Creates a Python object from JSON string representation

    Args:
        JSON string object representation

    Retruns:
        an object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
