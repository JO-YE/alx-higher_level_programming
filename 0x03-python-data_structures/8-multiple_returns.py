#!/usr/bin/python3
def multiple_returns(sentence):
    lent = len(sentence)
    if lent == 0:
        new_tuple = (lent, None)
    else:
        new_tuple = (lent, sentence[0])
    return (new_tuple)
