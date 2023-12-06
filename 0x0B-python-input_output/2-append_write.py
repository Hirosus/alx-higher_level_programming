#!/usr/bin/python3
"""
This module provides functions for file operations.

It includes functions to read, write, and append to text files.
"""

def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF8) and return the number of characters added.

    :param filename: The name of the file to be appended.
    :type filename: str
    :param text: The string to be appended to the file.
    :type text: str
    :return: The number of characters added to the file.
    :rtype: int
    """
    with open(filename, 'a', encoding='utf-8') as file:
        char_count = file.write(text)
    return char_count

