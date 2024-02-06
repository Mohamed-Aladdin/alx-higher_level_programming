#!/usr/bin/python3
"""module of read file function"""


def read_file(filename=""):
    """read a file"""

    with open(filename, "r", encoding="utf-8") as file:
        line = file.read()
        print(line, end="")
