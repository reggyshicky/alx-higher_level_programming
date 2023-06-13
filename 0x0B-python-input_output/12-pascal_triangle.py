#!/usr/bin/python3
"""module documentation"""


def pascal_triangle(n):
    """
    defines Pascal traingle of size and returns a
    list of lists onf ints representing the triangle
    """

    if n <= 0:
        return []
    triangle = [[1]]
    for w in range(1, n):
        row = [1]
        prev_row = triangle[w - 1]
        for x in range(1, w):
            row.append(prev_row[x - 1] + prev_row[x])
        row.append(1)
        triangle.append(row)
    return triangle
