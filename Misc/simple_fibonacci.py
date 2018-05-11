# Fibonacci Series :
# The sum of two elements defines the next.

a, b = 0, 1   #line contains multiple assignment.
while b < 10: # the "while" loop executes as long as consition remains true
    print(b) # The body of loop is indented: indentetion is python's way of grouping statements
    a , b =  b , a + b


a , b = 0 , 1
while b < 10000:
    print(b, end=',')
    a, b = b , a + b


# Note: Since '**' has more preference than '-', -3**2 ==> -(3**2)


##Using Functions
def fib(n):
    '''Print a fibonacci series upto n'''
    a, b = 0, 1
    while a < n:
        print(a, end=',')
        a , b = b , a + b
        print()

## Writing a function that returns a list of numbers of fibonacci, instead of printing it.

def fib2(n): # return fibonacci series upto n,
     result= []
     a , b = 0, 1
     while a < n:
         result.append(a) # this is equivalent to result = result +  [a], but more efficient.
         a, b = b , a + b
    return result

    
