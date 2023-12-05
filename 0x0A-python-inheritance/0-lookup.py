#!/usr/bin/python3
def lookup(obj):
    """Returns a list of available attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list containing the attributes and methods of the object.
    """
    return [attribute for attribute in dir(obj)]


