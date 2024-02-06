#!/usr/bin/python3
"""module of json file function"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n
    """

    if n <= 0:
        return []
    result = []
    arr = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if i == 0 or j == 0 or i == j:
                row.append(1)
            else:
                row.append(arr[j] + arr[j - 1])
        arr = row
        result.append(row)

    return result
