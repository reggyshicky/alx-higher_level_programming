#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)  # no. of rows/length of the matrix
    columns = len(matrix[0])  # length of the first row in matrix

    if matrix == [[]]:
        print()

    for x in range(rows):
        for w in range(columns):
            if w == columns - 1:
                print("{:d}".format(matrix[x][w]))
            else:
                print("{:d}".format(matrix[x][w]), end=" ")
