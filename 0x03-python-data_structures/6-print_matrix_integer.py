#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for z, digit in enumerate(row):
            if z == len(row) - 1:
                print("{:d}".format(digit))
            else:
                print("{:d}".format(digit), end=" ")
