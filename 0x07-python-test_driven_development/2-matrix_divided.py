#!/usr/bin/python3
"""
module 2-matrix_divided:
    contains implementation of matrix_divided() function

    Functions:
        matrix_divided(): function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function to divide all elemnts of a matrix

    Args:
        matrix: List of lists of int or float
        div: number to divide the matrix with. Must be a number(int/float)
    Return:
        A new matrix same size with the original matrix with all elemnts
        divided
    """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    res = []
    len_0 = len(matrix[0])
    if len_0 == 0:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
        if len(row) != len_0:
            raise TypeError("Each row of the matrix must have the same size")
        res_row = []
        for elem in row:
            if type(elem) != int and type(elem) != float:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
            res_row.append(round((elem / div), 2))
        res.append(res_row)

    return res
