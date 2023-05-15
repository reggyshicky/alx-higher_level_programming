#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return 0, None  # tuple with len 0 and None as 1st char

    x = len(sentence)
    char_1 = sentence[0]

    return x, char_1
