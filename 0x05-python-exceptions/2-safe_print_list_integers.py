#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count_integers = 0

    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count_integers += 1
        print()  # New line after printing integers
    except (IndexError, TypeError):
        pass

    return count_integers

