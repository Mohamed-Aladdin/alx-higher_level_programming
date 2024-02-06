#!/usr/bin/python3
"""module of json file function"""


class Student:
    """Represent a sample student"""

    def __init__(self, first_name, last_name, age):
        """Inits a new Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets dictionary representation of Student"""

        if type(attrs) is list and all([type(i) == str for i in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return (self.__dict__)

    def reload_from_json(self, json):
        """Reload stuff from json file"""
        for x, y in json.items():
            self.__dict__[x] = y
