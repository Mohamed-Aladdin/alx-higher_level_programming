#!/usr/bin/python3
"""module of write file function"""


def write_file(filename="", text=""):
    """
    writes to a text file and returns the number of characters written
    """

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

    return len(text)
