#!/usr/bin/python3
""" Print indented text Module"""


def text_indentation(text):
    """puts two new lines after these characters: . : ?
    Args:
        text: the given string
    Raises:
        TypeError: if the given text is not an str
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for symbol in ".:?":
        text = (symbol + "\n\n").join(
                [i.strip(" ") for i in text.split(symbol)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
