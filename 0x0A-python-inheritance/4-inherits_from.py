#!/usr/bin/python3
"""module of the same class function"""


def inherits_from(obj, a_class):
    """
    check if obj isinstance of a_class that is inherited
    Args:
        obj: the given object
        a_class: the given class
    """
    return isinstance(obj, a_class) and obj is not a_class
