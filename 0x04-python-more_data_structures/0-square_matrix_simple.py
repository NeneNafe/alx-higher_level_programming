#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result_mat = []

    for row in matrix:
        result = []

        for element in row:
            result.append(element ** 2)
        result_mat.append(result)
    return result_mat
