#!/usr/bin/python3
"""Print string in uppercase."""


def uppercase(str):
    # check for letters in the string given
    for letter in str:
    # is any of the letter lowercase
        if letter >= chr(97) and letter <= chr(122):
    # If yes,take out 32 from the ascii table to change to upper
            letter = chr(ord(letter) - 32)
# ord convert given letter to intergar
# chr convert to character
        print("{}".format(letter), end="")
    print("")
