#! /usr/bin/env python3

temps = [("Delhi", 34), ("Mumbai", 24),("Nagpur", 44),("Hyderabad", 35), ("Bangalore", 40)]

cel_to_far = lambda data : (data[0], (9/5)*data[1] + 32)
converted_list= list(map(cel_to_far,temps))

print(converted_list)

