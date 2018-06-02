#! /usr/bin/env python3
# chmod a+x sorted_words.py | to create executable.

# Program to sort alphabetically the words form a string provided by the user

# change this value for a different result
my_str = "Hello World, the sorting will be case sensitive. \
 They day its Ascii values that matters."

# uncomment to take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = my_str.split()

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
