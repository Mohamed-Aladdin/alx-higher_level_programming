#!/usr/bin/python3
"""module of the same class function"""


def is_kind_of_class(obj, a_class):
    """
    check if object is any kind of  a class.
    Args:
        obj: the object we are looking up
        a_class: the given class
    """

    return isinstance(obj, a_class)
