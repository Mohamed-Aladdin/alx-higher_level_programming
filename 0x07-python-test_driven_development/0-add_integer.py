#!/usr/bin/python3
"""Addition of Ints Module"""


def add_integer(a, b=98):
    """Return the addition of two integers or floats as integers

    Args:
        a: first arg
        b: second arg

    Returns:
        Addition of the two args

    Raises:
        TypeError: If any of the two args not an integer or a float
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
