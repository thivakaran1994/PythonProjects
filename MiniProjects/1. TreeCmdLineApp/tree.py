"""
This is an implementation of minimal version of tree linux command
using Python which recursively list or display the content of a
directory in a tree-like format.
"""

import os
import sys

from argument_parser import TreeArgMgr
from data_structures import Tree, Node


class TreeApp(object):
    """Tree CmdLine App"""
    
    def __init__(self):
        arg_mgr = TreeArgMgr()
        self._args = arg_mgr.get_args()
        self._directory_list = arg_mgr.directory_list
    
    def launch(self):
        """Entry point to the app"""
        self._validate_input_args()
        self._run()

    
    def _validate_input_args(self):
        """Validate the format and accuracy of input args"""
        if self._args.help:
            print(TreeArgMgr.help_msg)
            sys.exit(0)  # graceful exit

        for opt in self._directory_list:
            if opt.startswith("-"):
                # Unknow option
                print("tree: Invalid argument '{}'.".format(opt))
                print(TreeArgMgr.usage_msg)
                sys.exit(0)
    
    def _run(self):
        """
        Make tree for each input directory and display it to stdout
        """
        for dir_ in self._directory_list:
            tree = Tree(dir_)
            tree.make()
            self._display_tree(tree, tree.root)
    
    def _display_tree(self, tree: Tree, node: Node, indentation: int=0):
        """
        Displays the directory tree structure to stdout
        :parm tree : Tree which holds all the content
        :param node: Current Node
        :param indentation: This corresponds to the depth at which
                            a node is available in an N-ary tree
        :return: None
        """
        file_or_dir_name = os.path.basename(node.data)

        if not node.parent_node: # If it is a root node
            if not os.path.exists(node.data) or os.path.isfile(node.data):
                output = "%s [error opening dir]" % file_or_dir_name
            else:
                output = tree.user_given_top_directory

        elif indentation == 0:
            output = file_or_dir_name

        elif indentation == 1:
            output = "|__ %s" % file_or_dir_name

        else:
            output = "|%s|__ %s" % ((indentation - 1) * "   ", file_or_dir_name)

        if self._args.dirs_only:
            if os.path.isdir(node.data) or (node.parent_node is None):
                print(output)
        else:
            print(output)

        for child in node.children:
            # Increment indentation by one as the immediate child node
            # is one depth below the parent node
            if self._args.no_indent:
                self._display_tree(tree, child, indentation)
            else:
                self._display_tree(tree, child, indentation + 1)


if __name__ == "__main__":
    app = TreeApp()
    app.launch()