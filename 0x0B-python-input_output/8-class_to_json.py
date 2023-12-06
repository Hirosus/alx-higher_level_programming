#!/usr/bin/python3
"""
This module provides a function for JSON serialization.
"""

def class_to_json(obj):
    """
    Return a dictionary description for JSON serialization of an object.

    :param obj: An instance of a Class with serializable attributes.
    :return: A dictionary representation of the object for JSON serialization.
    :rtype: dict
    """
    # Check if obj is an instance of a Class
    if not hasattr(obj, '__dict__'):
        raise TypeError(f"{type(obj).__name__} is not serializable")

    # Serialize attributes of the object
    serialized_data = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized_data[key] = value

    return serialized_data

