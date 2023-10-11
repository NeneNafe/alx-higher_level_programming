#!/usr/bin/python3
"""Defines a function"""


def append_after(filename="", search_string="", new_string=""):
    """
    a function that inserts a line of text to a file, after each line
    containing a specific string
    """

    lines_to_insert = ""
    with open(filename) as r:
        for line in r:
            lines_to_insert += line
            if search_string in line:
                lines_to_insert += new_string
    with open(filename, 'w') as w:
        w.write(lines_to_insert)
