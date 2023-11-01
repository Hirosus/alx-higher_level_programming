#!/usr/bin/python3
for i in range(122, 96, -1):
    print("{}".format(chr(i)), end="")
    if i % 2 != 0:
        print("{}".format(chr(i - 32)), end="")
