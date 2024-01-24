#!/usr/bin/python3
"""Print Square Module"""


def print_square(size):
    """prints a square consisting of #

    Args:
        size: the length of one side.
    Raises:
        TypeError: if size is not equal int
        ValueError: if size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
