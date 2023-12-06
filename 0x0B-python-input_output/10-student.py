#!/usr/bin/python3
"""
This module defines the Student class.
"""

class Student:
    """
    Defines a student with first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with given attributes.

        :param first_name: The first name of the student.
        :param last_name: The last name of the student.
        :param age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        :param attrs: A list of attribute names to retrieve (default is None).
        :type attrs: list or None
        :return: A dictionary representation of the Student instance.
        :rtype: dict
        """
        if attrs is None:
            return self.__dict__

        filtered_data = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_data[attr] = getattr(self, attr)
        return filtered_data

