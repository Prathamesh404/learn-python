# Prime number are divisibleby self and 1.
import time


# Version 1
#1.Test all divisors from 2 through n - 1
#2. Skip (1 and n)


def is_prime_1(n):
    """
    Return "True" if 'n' is prime number. False otherwise.
    """
    if n == 1:
        return False # 1 is not prime.

    for d in range(2, n):
        if n % d == 0:
            return False
    return True

#++==================
# TEST FUNCTION.
#=====================

for n in range(1,21):
    print(n, is_prime_1(n))

#+++++++++++++++++++
#====V2============>
#+++++++++++++++++++

def is_prime_2(n):
    """ True if Prime, False otherwise"""
    if n == 1:
        return False # Not a prime

    max_div = math.floor(math.sqrt(n))
    for d in range(2, 1+max_div):
        if n % d == 0
        return False

    return True

#>>>>> Test 
for n in range(1,21):
    print(n, is_prime_2(n))



#+++++++++++++++++++
#====V3============>
# Eliminating the even numbers.
#+++++++++++++++++++

def is_prime_3(n):
    """ True if 'prime', False otherwise"""

    if n == 1:
        return False

    #If it's even and not 2 , then it's not prime.
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_div = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_div, 2):
        if n % d == 0:
            return False
    return True

#>>>>> Test
for n in range(1,21):
    print(n, is_prime_2(n))
