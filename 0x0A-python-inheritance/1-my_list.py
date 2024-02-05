#!/usr/bin/python3
"""module of the MyList class"""


class MyList(list):
    """MyList Class"""

    def print_sorted(self):
        """print sorted list function"""

        print(sorted(self))
