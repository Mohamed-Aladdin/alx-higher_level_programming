#!/usr/bin/python3
"""My Node module"""


class Node:
    """Defines a node"""

    def __init__(self, data, next_node=None):
        """This is init"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter"""

        return self.__data

    @data.setter
    def data(self, value):
        """data setter"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next node getter
        Returns: The next node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next node setter"""

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Define a SSL"""

    def __init__(self):
        """This is init"""

        self.head = None

    def __str__(self):
        """To print the nodes of the SSL
        Returns: The printed SLL"""

        sll = ""
        pos = self.head

        while pos:
            sll += str(pos.data) + "\n"
            pos = pos.next_node
        return sll[:-1]

    def sorted_insert(self, value):
        """Insert a node sorted
        Args:
            value: The node's value"""

        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        pos = self.head
        while pos.next_node and pos.next_node.data < value:
            pos = pos.next_node

        if pos.next_node:
            new_node.next_node = pos.next_node

        pos.next_node = new_node
