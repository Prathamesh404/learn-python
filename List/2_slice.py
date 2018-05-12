# ------------ Slcing the LIst ------------

# a[start:end] -> items start through end-1
# a[start:] ->  items starts through the rest of the array.
# a[:end] -> items through beginning through end -1
# a[:] --> copy the whole array(Shallow copy, not a recommended method)

# CLASSIC NOTATION
# a[start:end:step] # start through not past end, by step mentioned.

# -------------- Example -------------------

a = [2 ,3 ,5, 7, 9 , 11, 13, 17 , 19, 23]
print(a[-1]) # last item, we know that -> 23
print(a[-2:]) # Last two items in array -> [19, 23]

# +---+---+---+---+---+---+---+
# | P | A | N | D | O | R | A |
#   0   1   2   3   4   5   6
 # -7  -6  -5  -4  -3  -2  -1

 print(a[::-1]) # all items, reversed
 print(a[1::-1]) # First two items, reversed.
 print(a[:-3:-1]) # Last two items, reversed .
 print(a[-3::-1]) # Everything except last two items, reversed.
   
