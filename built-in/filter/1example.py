#!/usr/bin/env python3


l = [12, 45, 67, 90, 78]
evens = list(filter(lambda x: x % 2 == 0, l))
print(evens)

names = ["Piryanka","Prathamesh","Saket","Pishe", "Meg","Ashwi"]
p_names = list(filter(lambda n : n[0] == "P", names))
print(p_names)
