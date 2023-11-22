#!/usr/bin/python3

def raise_exception():
    try:
        raise TypeError("Exception raised")
    except TypeError as e:
        # Handling the raised exception
        print(e)

# Uncomment the line below to test the function
# raise_exception()

