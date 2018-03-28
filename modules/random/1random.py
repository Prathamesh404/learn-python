#Display 10 random numbers from interval(1,10)

import random
"""
for i in range(10):
    print(random.random())
"""
#Generate random number in given speicific range.

"""for i in range(10):
    print(random.uniform(3,7))
"""

#Understanding the normal distribution (aka Bell Curve)
#Standard Deviation & Mean.
#normalvariate(mean, standard deviation)
for i in range(20):
    print(random.normalvariate(3,3))

#Using randint for displaying integer in a speicific range
for i in range(20):
    print(random.randint(1,6))

# To select a element from an arrat or make a choice.
outcomes= ["rock", "paper", "scissors"]

for i in range(20):
    print(random.choice(outcomes))
