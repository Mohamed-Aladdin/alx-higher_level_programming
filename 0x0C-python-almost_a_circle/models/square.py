#!/usr/bin/python3
"""My Square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a sqaure"""

    def __init__(self, size, x=0, y=0, id=None):
        """Inits the square class"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """method to display the string rep of the square"""

        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size attr getter"""

        return self.width

    @size.setter
    def size(self, value):
        """size attr setter"""

        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """method to update the attr of the square"""

        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """method to update"""

        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """method to display the dictionary rep of the square"""

        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
