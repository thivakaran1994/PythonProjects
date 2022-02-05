"""
This is an implementation of an Argument manager module for Tree CmdlineApp
"""

# Load libraries
import argparse
import sys


class TreeArgMgr(object):
    """
    Argument Manager class for Tree cmd_line app
    """
    usage_msg = "usage: tree [--help] [-a] [-d] [-i] [<directory list>]\n"
    help_msg = ("%s"
        "------- Listing options -------\n"
        "-a            All files are listed.\n"
        "-d            List directories only.\n"
        "------- Graphics options -------\n"
        "-i            Don't print indentation lines.\n"
        "------- Miscellaneous options -------\n"
        "--help        Print usage and this help message and exit.\n"
        ) % usage_msg

    def __init__(self):
        self._parser =  argparse.ArgumentParser(
            prog="tree", allow_abbrev=False, add_help=False)
        self._add_arguments()
        self._args, self._res = self._parser.parse_known_args()

    def _add_arguments(self):
        """Adding options to parser"""
        miscellaneous_opts = self._parser.add_argument_group("Miscellaneous options")
        miscellaneous_opts.add_argument(
            "--help",
            dest="help",
            action="store_true",
            help="Print usage and this help message and exit."
        )

        listing_opts = self._parser.add_argument_group("Listing options")
        listing_opts.add_argument(
            "-a",
            dest="list_all",
            help="All files are listed.",
            default=True,
            action="store_true"
        )
        listing_opts.add_argument(
            "-d",
            dest="dirs_only",
            help="List directories only.",
            default=False,
            action="store_true"
        )

        graphic_opts = self._parser.add_argument_group("Graphics options")
        graphic_opts.add_argument(
            "-i",
            dest="no_indent",
            help="Don't print indentation lines.",
            action="store_true",
            default=False
        )

    def get_args(self):
        """Returns the value of protected attribute"""
        return self._args
    
    @property
    def directory_list(self):
        """Returns the path to input source file if specified.
           Else return the current working directory or '.'
        """
        if self._res:
            return self._res
        return ["."]