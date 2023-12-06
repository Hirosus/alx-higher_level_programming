#!/usr/bin/python3
"""
This module provides functions for JSON operations.
"""

import json

def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    :param filename: The name of the JSON file to load the object from.
    :return: The object represented by the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

