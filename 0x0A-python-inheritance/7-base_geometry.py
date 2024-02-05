#!/usr/bin/python3
"""module of the BaseGeometry class"""


class BaseGeometry():
    """BaseGeometry Class"""

    def area(self):
        """to calculate the area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        to validate the value
        Args:
            name (string): name
            value(int): Value
        Raises:
            TypeError: When Value is not int
            ValueError: When Value less or equal to 0
        """

        if !isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
