#!/usr/bin/python3
"""
This module provides functions for file operations.

It includes functions to read and write text files.
"""

def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters written.

    :param filename: The name of the file to be written.
    :type filename: str
    :param text: The string to be written to the file.
    :type text: str
    :return: The number of characters written to the file.
    :rtype: int
    """
    with open(filename, 'w', encoding='utf-8') as file:
        char_count = file.write(text)
    return char_count

