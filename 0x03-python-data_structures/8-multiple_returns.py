#!/usr/bin/python3
def multiple_returns(sentence):
    x = 0
    for i in sentence:
        x += 1
    return x, sentence[0]
