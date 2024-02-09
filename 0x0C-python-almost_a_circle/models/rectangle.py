#!/usr/bin/python3
"""My Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """Defines a rectangle"""

    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Inits the base class"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width attr getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """width attr setter"""

        self.validate_int("width", value, False)
        self.__width = value

    @property
    def height(self):
        """height attr getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """height attr setter"""

        self.validate_int("height", value, False)
        self.__height = value

    @property
    def x(self):
        """x attr getter"""

        return self.__x

    @x.setter
    def x(self, value):
        """x attr setter"""

        self.validate_int("x", value)
        self.__x = value

    @property
    def y(self):
        """y attr getter"""

        return self.__y

    @y.setter
    def y(self, value):
        """y attr setter"""

        self.validate_int("y", value)
        self.__y = value

    def validate_int(self, var, value, fg=True):
        """method to validate int values"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(var))
        if fg and value < 0:
            raise ValueError("{} must be >= 0".format(var))
        elif not fg and value <= 0:
            raise ValueError("{} must be > 0".format(var))

    def area(self):
        """method to calculate the area"""

        return self.width * self.height

    def display(self):
        """method to display the rectangle instance"""

        rep = "\n" * self.y + \
            (" " * self.x + "#" * self.width + "\n") * self.height
        print(rep, end="")

    def __str__(self):
        """method to print the str instance of the rectangle"""

        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """method to update attr"""

        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """method to assign an argument to each attribute"""

        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """method to display the dictionary rep of the rectangle"""

        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
