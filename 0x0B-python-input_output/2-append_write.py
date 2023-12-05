#!/usr/bin/python3

def append_write(filename="", text=""):
    """Append a string to the end of a text file and return the number of characters added.

    Args:
        filename (str): The name of the text file.
        text (str): The string to append.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        characters_added = file.write(text)
    return characters_added
