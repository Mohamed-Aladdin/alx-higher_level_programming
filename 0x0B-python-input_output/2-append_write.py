#!/usr/bin/python3
"""module of append file function"""


def append_write(filename="", text=""):
    """
    appends to a text file and returns the number of characters written
    """

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
