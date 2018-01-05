def iterative_factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result


for i in range(1, 100):
    print(i , ":", iterative_factorial(i))
