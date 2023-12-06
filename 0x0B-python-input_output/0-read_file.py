#!/usr/bin/python3
"""
This module provides functions for file operations.

It includes a function to read a text file and print its content to stdout.
"""

def read_file(filename=""):
    """
    Read the content of a text file (UTF8) and print it to stdout.

    :param filename: The name of the file to be read.
    :type filename: str
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')


