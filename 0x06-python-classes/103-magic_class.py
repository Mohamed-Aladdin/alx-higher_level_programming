#!/usr/bin/python3
"""writing Magic"""

import math


class MagicClass:
    """My Magic Class"""

    def __init__(self, radius=0):
        """ Magic Class init """
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """To calculate the area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """To calculate the circumference"""
        return 2 * math.pi * self.__radius
