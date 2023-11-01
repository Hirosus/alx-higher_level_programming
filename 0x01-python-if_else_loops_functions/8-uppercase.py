#!/usr/bin/python3
def to_uper(character):
    if ord(character) >= 97 and ord(character) <= 122:
        return chr(ord(character) - 32)
    else:
        return character

def uppercase(string):
    string_new = ""
    for character in string:
        string_new += chr(to_uper(character))
    print(string_new)
