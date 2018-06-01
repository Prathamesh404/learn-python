#! /usr/bin/env python3

from random import random

def flip_coin():
    #generate random number 0-1
    r = random()
    if r > 0.5:
        return "Heads it is"
    else:
        return "Tails it is"

print(flip_coin())

