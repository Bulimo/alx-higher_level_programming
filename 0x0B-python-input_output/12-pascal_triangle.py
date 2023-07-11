#!/usr/bin/python3
"""
Module 12-pascal_triangle

Functions:
    pascal_triangle(n)
"""


def pascal_triangle(n):
    """
     Returns the Pascal’s triangle of n

     Args:
        n(int): size of the Pascal's triangle

    Returns:
        List of list of Pascal's triangle
    """
    if n <= 0:
        return pascal

    pascal = [[1]]
    for c in range(1, n):
        row = [1]
        if c > 1:
            for i in range(1, len(pascal[c - 1])):
                row.append(pascal[c - 1][i - 1] + pascal[c - 1][i])
        row.append(1)
        pascal.append(row)

    return pascal
