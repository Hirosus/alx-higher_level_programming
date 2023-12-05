#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text into a file after each line containing a specific string.

    Args:
        filename (str): The name of the text file.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after lines containing the search string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
