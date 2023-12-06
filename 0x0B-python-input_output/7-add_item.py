#!/usr/bin/python3
"""
Script to add command line arguments to a Python list and save them to a JSON file.
"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Get existing data from file or create an empty list
try:
    existing_data = load_from_json_file("add_item.json")
except (FileNotFoundError, json.decoder.JSONDecodeError):
    existing_data = []

# Add command line arguments to the list
new_data = sys.argv[1:]
updated_data = existing_data + new_data

# Save the updated list to the file
save_to_json_file(updated_data, "add_item.json")

