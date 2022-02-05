"""
This is an implementation of N_ary Tree data structure
"""

# Importing required libraries
import os
import sys


class Node(object):
    """
    Node in an N-ary Tree
    """
    def __init__(self, data, parent_node=None, children=None):
        self.data = data
        self.parent_node = parent_node
        self.children = children if children else []

    def add_child(self, child_node):
        """
        Add a child node to a particular nde
        :param child_node: <class 'Node'>
        :return: None
        """
        if child_node not in self.children:
            self.children.append(child_node)


class Tree(object):
    """
    Tree data structure to hold the structure of sub directories
    and files available under the root directory
    """
    def __init__(self, _input_dir: str = None):
        self.user_given_top_directory = _input_dir
        if _input_dir == ".":
            _input_dir = os.getcwd()
        self.root = Node(_input_dir)


    def make(self) -> None:
        """
        Recursively fill/complete the tree with all the
        available nested sub directories/files
        """
        self._find_and_add_children_of_node(self.root)

    def _find_and_add_children_of_node(self, parent_node: Node) -> None:
        """
        Find out the potential children nodes of a particular node
        and update that node
        """
        parent_dir = parent_node.data

        if not os.path.exists(parent_dir):
            return

        if os.path.isfile(parent_dir):
            return

        for ele in sorted(os.listdir(parent_dir)):
            child = Node(os.path.join(parent_dir, ele), parent_node)
            self._find_and_add_children_of_node(child)
            parent_node.add_child(child)
        return