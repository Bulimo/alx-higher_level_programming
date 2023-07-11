#!/usr/bin/python3
"""
Module 8-class_to_json

Functions:
    class_to_json()
"""


def class_to_json(obj):
    """
    Creates a dictionary description for JSON serialization of an object

    Args:
        obj: object to create dictionary

    Returns:
        dictionary description with simple data structure for JSON
        serialization of an object
    """
    import json
    return json.dumps(obj.__dict__)
