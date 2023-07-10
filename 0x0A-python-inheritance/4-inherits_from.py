#!/usr/bin/python3
"""
Module 4-inherits_from

A function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class

Args:
    obj: object to check
    a_class: class to compare with obj

Returns:
    True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    return issubclass(type(obj), a_class) and type(obj) != a_class
