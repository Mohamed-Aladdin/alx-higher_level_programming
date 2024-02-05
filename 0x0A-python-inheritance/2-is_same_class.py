#!/usr/bin/python3
"""module of the same class function"""


def is_same_class(obj, a_class):
    """
    checks class and instances
    Args:
        obj: the object we are looking up
        a_class: the given class
    """

    return type(obj) is a_class
