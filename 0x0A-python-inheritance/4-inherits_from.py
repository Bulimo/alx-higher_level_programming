#!/usr/bin/python3
"""
A function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: object to check
        a_class: class to compare with obj

    Returns:
        True if the object is an instance of a base class that it is
        been derived (directly or indirectly)
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
