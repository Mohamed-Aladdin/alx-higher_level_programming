#!/usr/bin/python3
"""module of json file function"""


def class_to_json(obj):
    """
    Returns dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """

    return (obj.__dict__)
