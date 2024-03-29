#!/usr/bin/python3
"""module of the lookup function"""


def lookup(obj):
    """
    returns a list of available attributes and methods of an object
    Args:
        obj: the object we are looking up
    Returns:
        a list object of attr
    """

    return dir(obj)
