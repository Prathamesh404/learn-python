#This program uses one of the important context of Dictionary- setdefault()
# setdefault(key, value)- this set a speific key and its value.
# We will also use a pprint module for pretty printing.

import pprint

poem = "let me be your electic meter, I will not run out.\
let me be your electic heater, you get cold without."
# We are counting the occurence of letters in this beautiful poem.
count= {}

for character in poem:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

