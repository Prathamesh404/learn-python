# Variable -> total=1
# Iterate through list, even num check
# If it is, mulitply total by num

def mult_even_nums(nums):
    total = 1
    for val in nums:
        if val % 2 == 0:
            total *= val
    return total
