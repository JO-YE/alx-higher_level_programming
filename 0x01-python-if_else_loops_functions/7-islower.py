#!/usr/bin/python3
def islower(c):
    """Function that checks for lowercasecharacters."""
    letter = 97
    letter2 = 122
#is the letter within a to z(lower)
    if c >= chr(letter) and c <= chr(letter2):
#if yes return true and false otherwise
        return True
    else:
        return False
