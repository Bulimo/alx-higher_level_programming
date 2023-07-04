#!/usr/bin/python3
"""
module 100-matrix_mul
"""


def matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices

    Args:
        m_a: Matrix of either type int or float
        m_b: matrix of either type int or float
    Return:
        product of matrix m_a and m_b
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if type(m_a[0]) != list:
        raise TypeError("m_a must be a list of lists")
    if type(m_b[0]) != list:
        raise TypeError("m_b must be a list of lists")

    len_a = len(m_a[0])
    len_b = len(m_b[0])

    for row in m_a:
        if type(row) != list:
            raise TypeError("m_a should contain only integers or floats")
        if len(row) == 0:
            raise ValueError("m_a can't be empty")
        if len_a != len(row):
            raise TypeError("each row of m_a must be of the same size")
        for elem in row:
            if type(elem) != int and type(elem) != float:
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        len_row = len(row)
        if type(row) != list:
            raise TypeError("m_b should contain only integers or floats")
        if len(row) == 0:
            raise ValueError("m_b can't be empty")
        if len_row != len_b:
            raise TypeError("each row of m_b must be of the same size")
        for elem in row:
            if type(elem) != int and type(elem) != float:
                raise TypeError("m_b should contain only integers or floats")
    if len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = []
    for row_a in m_a:
        res_row = [0] * len_b
        i, row_b = 0, 0
        while i < len(row_a) and row_b < len(m_b):
            j = 0
            while j < len(m_b[row_b]):
                res_row[j] += row_a[i] * m_b[row_b][j]
                j += 1
            i += 1
            row_b += 1
        res.append(res_row)
    return res
