#!/usr/bin/python3
"""
This module provides functions for JSON operations.
"""

import json

def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    :param my_obj: The object to be converted to JSON.
    :return: The JSON representation of the object as a string.
    :rtype: str
    """
    return json.dumps(my_obj)

