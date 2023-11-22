def raise_exception_msg(message=""):
    if message == "":
        raise NameError("C is fun")

# Example usage:
try:
    raise_exception_msg()
except NameError as ne:
    print(ne)

