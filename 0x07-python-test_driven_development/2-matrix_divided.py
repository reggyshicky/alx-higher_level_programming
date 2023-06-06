#!/usr/bin/python3
"""
Module for division of all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function to divide all elememnts of a matrix
    """
    new_mat = []
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or matrix is [[]] or matrix is None:
        raise TypeError(error)
    if type(div) is int or type(div) is float or type(div) is None:
        pass
    else:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix[0]:
        len_ = len(matrix[0])
    else:
        raise TypeError(error)
    for w in range(len(matrix)):
        if len(matrix[w]) is not len_:
            raise TypeError("Each row of the matrix must have the same size")
        new_mat.append([])
        for x in matrix[w]:
            if type(x) is int or type(x) is float:
                new_mat[w].append(round(x / div, 2))
            else:
                raise TypeError(error)
    return new_mat
