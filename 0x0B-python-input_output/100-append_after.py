#!/usr/bin/python3
"""
This module defines a function for appending text after specific lines in a file.
"""

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string.

    :param filename: The name of the file to modify.
    :type filename: str
    :param search_string: The string to search for in each line.
    :type search_string: str
    :param new_string: The line of text to insert after lines containing the search string.
    :type new_string: str
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

