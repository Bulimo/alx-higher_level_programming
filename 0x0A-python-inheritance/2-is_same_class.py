#!/usr/bin/python3
"""
Function that checks if an object is an object is exactly an instance of
of specified class

Args:
    obj: object to check
    a_class: class to check if obj is an instance

Returns:
    True if the object is exactly an instance of the specified class;
    otherwise, False.
"""


def is_same_class(obj, a_class):
    """
    Notes:
        use type() to get specific class
        use isinstance() to get class and any parent classes too
        use issubclass() to get what object is a subclass of
    Returns:
        True if obj is exactly an instance of specified class
    """
    return type(obj) is a_class
