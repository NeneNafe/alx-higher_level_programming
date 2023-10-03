#!/usr/bin/python3
"""A matrix function"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix
    where All elements of the matrix should be divided by div,
    rounded to 2 decimal places"""

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    row_len = []
    for row in matrix:
        row_len.append(len(row))
    if not all(element == row_len[0] for element in row_len):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(element / div, 2) for element in row] for row in matrix]

    return result
