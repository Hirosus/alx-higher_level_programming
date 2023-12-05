#!/usr/bin/python3
import json

def save_to_json_file(my_obj, filename):
    """Save an object to a JSON file.

    Args:
        my_obj (object): The object to be saved.
        filename (str): The name of the file.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

