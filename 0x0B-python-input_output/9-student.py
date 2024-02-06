#!/usr/bin/python3
"""module of json file function"""


class Student:
    """Represent a sample student"""

    def __init__(self, first_name, last_name, age):
        """Inits a new Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets dictionary representation of Student"""

        return self.__dict__
