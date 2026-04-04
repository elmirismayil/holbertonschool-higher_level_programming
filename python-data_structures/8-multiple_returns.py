#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence)==0:
        first_char = 0
    else:
        first_char = sentence[0]
    return (len(sentence),first_char)
