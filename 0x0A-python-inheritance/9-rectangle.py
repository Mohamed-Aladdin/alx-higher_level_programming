#!/usr/bin/python3
"""module of the Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(list):
    """Rectangle Class"""

    def __init__(self, width, height):
        """initiation method"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates the area of rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """str rep function for rectangle"""

        return("[Rectangle] {}/{}".format(self.__width, self.__height))
