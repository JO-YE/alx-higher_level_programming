#!/usr/bin/python3
"""Print string in uppercase."""
def uppercase(str):
#check for letters in the string given
    for l in str:
#is any of the letter lowercase
        if l >= chr(97) and l <= chr(122):
#If yes,take out 32 from the ascii table to change to upper
            l = chr(ord(l) - 32)
#ord convert given letter to intergar
#chr convert to character
        print("{}".format(l), end="")
    print("")
