#!/usr/bin/python3
"""
Module 100-singly_linked_list
Defines class Node (with private data and next_node)
Defines class SinglyLinkedList (with private head and public sorted_insert)
"""


class Node:
    """
    class Node definition

    Attributes:
        data (int): private
        next_node : private; can be None or Node object

    """

    def __init__(self, data, next_node=None):
        """
        Initializes node

        Attributes:
            data (int): private
            next_node : private; can be None or Node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """"
        Getter method

        Return: data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to update data value

        Args:
            value: sets data to value if int
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """"
        Getter method

        Return: next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to update next node

        Args:
            value: sets next_node if value is next_node or None
        """
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    class SinglyLinkedList definition

    Args:
        head: private.
            points to the start of the list

    """

    def __init__(self):
        """
        Initializes singly linked list

        Attributes:
            head: points to the start of the list. Initially None
        """
        self.__head = None

    def __str__(self):
        """
        String representation of singly linked list needed to print
        """
        string = ""
        tmp = self.__head
        while tmp:
            string += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """
        Inserts new nodes into singly linked list in sorted order

        Args:
        value: int data for node
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        tmp = self.__head
        if new.data < tmp.data:
            new.next_node = self.__head
            self.__head = new
            return

        while (tmp.next_node is not None) and (new.data > tmp.next_node.data):
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new
        return
