#!/usr/bin/python3
"""
This module provides functions for JSON operations.
"""

import json

def from_json_string(my_str):
    """
    Return a Python data structure represented by a JSON string.

    :param my_str: The JSON string to be converted to a Python object.
    :return: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)

