#!/usr/bin/python3
""""
Module for division of all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function to divide all elememnts of a matrix
    """
    for row in matrix:
        for elem in row:
            if type(elem) != int and type(elem) != float:
                raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")
    len_row = len(matrix[0])
    for row in matrix:
        if len(row) != len_row:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_mat = [[0 for _ in range(len(matrix[0]))]
               for _ in range(len(matrix))]
    for w in range(len(matrix)):
        for x in range(len(matrix[0])):
            new_mat[w][x] = round(matrix[w][x] / div, 2)

    return new_mat
