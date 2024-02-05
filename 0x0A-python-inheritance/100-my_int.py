#!/usr/bin/python3
"""module of the MyInt class"""


class MyInt(int):
    """MyInt Class"""

    def __eq__(self, other):
        """myint is a rebel, eq is !="""
        return int(self) != int(other)

    def __ne__(self, other):
        """myint is a rebel, ne is =="""
        return int(self) == int(other)
