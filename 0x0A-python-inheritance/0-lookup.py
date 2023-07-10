#!/usr/bin/python3
"""
Module 0-lookup : defines function to print the attributes of an object

Arguments:
    obj: any type. Object to get its attributes
Return:
    List of attributes found
"""


def lookup(obj):
    return dir(obj)
