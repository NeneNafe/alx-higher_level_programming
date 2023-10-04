#!/usr/bin/python3
"""This function contains a matrix of the multiples of 2"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """This fucntions returns the multiplication of two matrices.
    Args:
        m_as is the first matrix
        m_b is the second_matrix
    """

    return (np.matmul(m_a, m_b))
