#!/usr/bin/python3

class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        return {key: getattr(self, key) for key in self.__dict__}