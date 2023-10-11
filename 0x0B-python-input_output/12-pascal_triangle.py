#!/usr/bin/python3
"""Defines a function"""


def pascal_triangle(n):
    """
    Prints a pascals triangle
    """

    if n <= 0:
        return []

    p_triangle = []
    for i in range(n):
        if i == 0:
            p_triangle.append([1])
        else:
            prev_row = p_triangle[i - 1]
            new_row = [1]
            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j])
            new_row.append(1)
            p_triangle.append(new_row)

    return p_triangle
