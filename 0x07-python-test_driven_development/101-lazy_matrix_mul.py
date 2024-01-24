#!/usr/bin/python3
"""This module contains a function that mul two matrices"""

import numpy as nmp


def lazy_matrix_mul(m_a, m_b):
    """Return the mul of two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """

    return (nmp.matmul(m_a, m_b))


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/101-lazy_matrix_mul.txt")
