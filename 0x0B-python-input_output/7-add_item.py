#!/usr/bin/python3
import sys
from json import dump, load
from os.path import exists

def save_to_json_file(my_list, filename):
    """Save a list to a JSON file.

    Args:
        my_list (list): The list to be saved.
        filename (str): The name of the file.
    """
    with open(filename, 'w') as file:
        dump(my_list, file)

def load_from_json_file(filename):
    """Load a list from a JSON file.

    Args:
        filename (str): The name of the file.

    Returns:
        list: The loaded list.
    """
    if exists(filename):
        with open(filename, 'r') as file:
            return load(file)
    return []

if __name__ == "__main__":
    try:
        # Load existing items from file
        existing_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_items = []

    # Add new items from command line arguments
    new_items = sys.argv[1:]
    updated_list = existing_items + new_items

    # Save the updated list to the file
    save_to_json_file(updated_list, "add_item.json")

