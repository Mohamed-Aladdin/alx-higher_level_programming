#!/usr/bin/python3
"""My Base module"""

from json import dumps
from json import loads
import csv
import turtle


class Base:
    """Defines a base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Inits the base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """method to convert dictionary to json dump"""

        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """method to save to a file"""

        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]

        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") \
                as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """method to convert from json"""

        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """method to create an instance"""

        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None

        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """method to load from a file"""

        from os import path

        file = "{}.json".format(cls.__name__)

        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**arg) for arg in
                    cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """method to save to a csv file"""

        from models.rectangle import Rectangle
        from models.square import Square

        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                             for obj in list_objs]
            else:
                list_objs = [[obj.id, obj.size, obj.x, obj.y]
                             for obj in list_objs]

        with open('{}.csv'.format(cls.__name__), 'w', newline="",
                  encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """method to load from a csv file"""

        from models.rectangle import Rectangle
        from models.square import Square

        new = []

        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as file:
            reader = csv.reader(file)

            for row in reader:
                row = [int(r) for r in row]

                if cls is Rectangle:
                    string = {"id": row[0], "width": row[1], "height": row[2],
                              "x": row[3], "y": row[4]}
                else:
                    string = {"id": row[0], "size": row[1],
                              "x": row[2], "y": row[3]}
                new.append(cls.create(**string))
        return new

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        method to draw the rectangle and square classes using turtle module
        """

        tort = turtle.Turtle()
        tort.screen.bgcolor("#b7312c")
        tort.pensize(3)
        tort.shape("turtle")
        tort.color("#ffffff")

        for rec in list_rectangles:
            tort.showturtle()
            tort.up()
            tort.goto(rect.x, rect.y)
            tort.down()

            for i in range(2):
                tort.forward(rec.width)
                tort.left(90)
                tort.forward(rec.height)
                tort.left(90)
            tort.hideturtle()

        turt.color("#b5e3d8")

        for squ in list_squares:
            tort.showturtle()
            tort.up()
            tort.goto(squ.x, squ.y)
            tort.down()

            for i in range(2):
                tort.forward(squ.width)
                tort.left(90)
                tort.forward(squ.height)
                tort.left(90)
            tort.hideturtle()

        turtle.exitonclick()
