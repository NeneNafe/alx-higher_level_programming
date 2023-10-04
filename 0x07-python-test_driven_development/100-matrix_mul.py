#!/usr/bin/python3
"""Defines a Matrix Multiplication"""


def matrix_mul(m_a, m_b):
    """This is a function that multiplies 2 matrices by taking two
    arguments m_a and m_b, which must be validate with certain requirements"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [number for row in m_a for number in row]):
        raise TypeError("m_a should contain only integers or floats")

    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [number for row in m_b for number in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a args should be the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b args should be the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix1 = []
    for i in range(len(m_b[0])):
        the_row = []
        for j in range(len(m_b)):
            the_row.append(m_b[j][i])
        matrix1.append(the_row)

    matrix2 = []
    for row in m_a:
        the_row = []
        for column in matrix1:
            product = 0
            for m in range(len(matrix1[0])):
                product += row[m] * column[m]
            the_row.append(product)
        matrix2.append(the_row)

    return matrix2
