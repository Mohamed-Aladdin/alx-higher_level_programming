#!/usr/bin/python3
"""module for add_attribute function"""


def add_attribute(obj, name, value):
    """add an attribute to an object"""

    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    elif hasattr(obj, "__slots__") and name in obj.__slots__:
        setattr(obj, name, value)
    else:
        raise TypeError('can\'t add new attribute')
