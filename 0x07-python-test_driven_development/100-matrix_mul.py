#!/usr/bin/python3
"""Matrix mul Module"""


def matrix_mul(m_a, m_b):
    """This function mul two matrices

    Args:
        m_a (list of lists of int/float): Matrix to be mul
        m_b (list of lists of int/float): Matrix to be mul

    Raises:
        TypeError: If m_a or m_b is not a list
        TypeError: If m_a or m_b is not a list of lists
        TypeError: If one element of list of lists is not int/float
        TypeError: If row of m_a or m_b are not the same size
        ValueError: If m_a or m_b is empty
        ValueError: If m_a and m_b cannot be multiplied

    Returns:
        A new list which is the outcome of the multiplication
    """

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

    if not all((isinstance(item, int) or isinstance(item, float))
               for item in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(item, int) or isinstance(item, float))
               for item in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m1 = []
    for x in range(len(m_b[0])):
        temp = []
        for y in range(len(m_b)):
            temp.append(m_b[y][x])
        m1.append(temp)

    m2 = []
    for row in m_a:
        temp = []
        for col in m1:
            mul = 0
            for x in range(len(m1[0])):
                mul += row[x] * col[x]
            temp.append(mul)
        m2.append(temp)

    return m2


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/100-matrix_mul.txt")
