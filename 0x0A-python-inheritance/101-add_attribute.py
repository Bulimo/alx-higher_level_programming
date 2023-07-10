#!/usr/bin/python3
"""
Module 101-add_attribute

Functions:
    add_attribute()
"""


def add_attribute(obj, attr, value):
    """
    Add attribute to the object if possible
    Args:
        obj: object to add attribute
        attr: attribute to be added
        value: the value to be added
    Returns:
        raises exception if unable to add attribute
    """
    invalid_types = [int, float, complex, str, bytes, bytearray, list, tuple,
                     dict, set, frozenset, bool, None]
    if type(obj) in invalid_types:
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
