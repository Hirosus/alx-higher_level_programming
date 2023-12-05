#!/usr/bin/python3
import json

def to_json_string(my_obj):
    """Convert a Python object to a JSON string.

    Args:
        my_obj (object): The object to be serialized.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
