#!/usr/bin/python3

def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary representation of the object with serializable attributes.
    """
    return {key: getattr(obj, key) for key in obj.__dict__ if type(getattr(obj, key)) in (list, dict, str, int, bool)}
