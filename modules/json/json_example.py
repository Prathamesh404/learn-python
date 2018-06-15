#! /usr/bin/env python3
import json

numbers = [2,3,5,7,11,13]
filename = 'numbers.json'
with open(filename) as f_obj:
    json.dump(numbers, f_obj)

""" Load some previously stored numbers"""
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

# making sure the stored data exists.
f_name = 'numbers.json'
try:
    with open(f_name) as f_obj:
        numbers = json.load(f_obj)
except FileNotFoundError:
    msg= f"Can't find {f_name}"
    print(msg)
else:
    print(numbers)
