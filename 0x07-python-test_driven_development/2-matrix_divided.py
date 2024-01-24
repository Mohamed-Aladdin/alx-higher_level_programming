#!/usr/bin/python3
"""Division of a list of lists of Ints Module"""


def matrix_divided(matrix, div):
    """divides matrix items by div
    Args:
        matrix: a list of lists containing ints or floats
        div: the given int or float number
    Raises:
        TypeError: if matrix isn't a list of lists with ints or floats
        TypeError: if 2D lists are not the same len
        TypeError: if div is not float or integer
        ZeroDivisionError: if div == 0
    Returns:
        list of lists containing divided elements
    """

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for arr in matrix:
        if not isinstance(arr, list) or len(arr) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(arr) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for num in arr:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(num / div, 2) for num in arr] for arr in matrix]


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/2-matrix_divided.txt")
