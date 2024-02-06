#!/usr/bin/python3
"""module of json file function"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts line to file,
    after each line containing specific string
    """

    with open(filename, "r+", encoding="utf-8") as file:
        s = ""
        for line in file:
            s += line
            if search_string in line:
                s += new_string
        file.seek(0)
        file.write(s)
