#!/usr/bin/python3
"""
Create a locked class allowing only 'first_name' as a dynamic instance attribute
"""


class LockedClass:
    """
    A class that prevents the instantiation of attributes except for 'first_name'.
    """

    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        """
        Initializes 'first_name'.
        """
        self.first_name = first_name

