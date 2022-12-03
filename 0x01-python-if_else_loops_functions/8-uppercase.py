#!/usr/bin/python3
"""Print string in uppercase."""


def uppercase(str):
    for letter in str:
        if letter >= chr(97) and letter <= chr(122):
            letter = chr(ord(letter) - 32)
# ord convert given letter to intergar
# chr convert to character
        print("{}".format(letter), end="")
    print("")
