#! /usr/bin/env python3
# Display 10 random numbers from interval [0,1)
import random

for i in range(10):
    print(random.random())

# understanding Normal Distribution(AKA Bell Curve)
#for i in range(20):
#    print(random.normalvariate(0,0.2))

# Creating random numbers in a range. Integers.
for i in range(20):
    print(random.randint(1,10))

# taking random choices from a list.
outcomes = ["failed", "success", "middle"]

for i in range(10):
    print(random.choice(outcomes))

