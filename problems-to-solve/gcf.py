# This program deals with finding Greatest Common Divisor.

def gcf(num1, num2):
    if num1 > num2: # We need to create this case to realize that a smaller number among the two numbers is the biggest GCF possible.
        #Thus we create a range according to it.
        num1, num2 = num2, num1

    for x in range (num1, 0, -1):
        if num1 % x == 0 and num2 % x == 0:
            return x


print(str(gcf(324, 576)))
