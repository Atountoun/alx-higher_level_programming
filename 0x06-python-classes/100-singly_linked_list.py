#!/usr/bin/python3
"""Module that contains class Node and class SinglyLinkedList."""


class Node:
    """A class Node that defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """The class Node constructor.

        Args:
            data (int): the node's value
            next_node (Node): the next node of this current node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """The method data use as getter property of a value at a node."""
        return self.__data

    @data.setter
    def data(self, value):
        try:
            self.__data = int(value)
        except Exception:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """The property used to set and get the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list."""

    def __init__(self):
        """The class SinglyLinkedList constructor"""
        self.__head = None

    def sorted_insert(self, value):
        """The method for insertion into the linked list

        This method is used to insert a new Node into the correct
        sorted position in the list(increasing order).

        Args:
            value (Node): the content of the new node to be inserted
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_node = self.__head
            prev_node = self.__head
            while current_node is not None:
                if value < current_node.data:
                    prev_node.next_node = new_node
                    new_node.next_node = current_node
                    return
                prev_node = current_node
                current_node = current_node.next_node
            else:
                prev_node.next_node = new_node
                new_node.next_node = None

    def __str__(self):
        """The method that prints the representaion of the list."""
        nodes_datas = []
        current_node = self.__head
        while current_node is not None:
            nodes_datas.append(str(current_node.data))
            current_node = current_node.next_node
        return ('\n'.join(nodes_datas))
