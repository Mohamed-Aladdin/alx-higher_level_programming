#!/usr/bin/python3
"""My Square module"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Create a Square

        Args:
            size: length of side

        Raises:
            TypeError: if size != int
            ValueError: if size < 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Get the area of a Square

        Returns: The size squared
        """

        return self.__size * self.__size
