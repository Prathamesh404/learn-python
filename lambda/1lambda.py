#! /usr/bin/env python3
# A regular named function.
def square(num): return num*num

# Equivalent lambda function
square2 = lambda num: num*num

#And one more
add = lambda a,b : a + b

#And one for the cube
cube = lambda num: num**3

# Execute the functions.
print(square2(34))
print(add(3,6))
print(cube(30))



# An important notification, does lambda have names.
print(square.__name__)
print(square2.__name__)
print(add.__name__)
print(cube.__name__)

