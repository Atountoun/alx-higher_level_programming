#!/usr/bin/python3
class Node:
    """A class Node that defines a node of a singly linked list."""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """The method data use as getter property of a value at a node."""
        return self.__data

    @data.setter
    def data(self, value):
        """The method data use as setter of the value of a node."""
        try:
            self.__data = int(value)
        except Exception:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """The method next_node use as a getter property that indicates the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """The setter method as property to set the next_node of a given node.
        Args:
            value: the value to be set to next_node
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list."""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """This method is used to insert a new Node into the correct
        sorted position in the list(increasing order).
        Args:
            value: the content of the new node to be inserted
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            current_node = self.__head
            prev_node = self.__head
            while current_node is not None:
                if value < current_node.data:
                    prev_node.next_node = new_node
                    new_node.next_node = current_node
                    break
                prev_node = current_node
                current_node = prev_node.next_node

    def __str__(self):
        current_node = self.__head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
