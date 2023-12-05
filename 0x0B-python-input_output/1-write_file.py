#!/usr/bin/python3

def write_file(filename="", text=""):
    """Write a string to a text file and return the number of characters written.

    Args:
        filename (str): The name of the text file.
        text (str): The string to write.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        characters_written = file.write(text)
    return characters_written

