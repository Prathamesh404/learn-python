# Functions in Python

#### What is a Function? Why?
- A process for executing a task.
- Can accept input or return an output(_not mandatory_)
- Important context in __D__on't __R__epeat __Y__ ourself methodology. Executing similar procedures over and over.
- Clean up and prevent code duplication.
- The Abstraction is created for other user(when ya building that awesome framework for a community)

#### Structure and Examples.
  ```Python
      #simples way of defining.
      def name_of_function():
        pass
  ```

  ```Python
      def birthday_song():
        return "Happy Birthday to You"
  ```
#### Return Values.
- It basically exits the function.
- Function without the __return__ statement actaully returns None.
- When the computer returns from a function, it _picks up where it left off_  before the function call. In short, it Pops the function off the call stack.

```Python
def print_square(x):
  return x**2

def greet():
  return "Hello, Deer"

greeting = greet()
print(greeting) # "Hello, Deer"    
```

#### Functions with Parameters.
- A function accepts a parameter as a input.
- _Parameters_ are the variables to a function - thinking of them as placeholders that get assigned when you call a function.

```python
def square(num):
    return num * num

square(6) # 36

def birth_person(name):
  return (f"Happy Birthday to {name}")

birth_person("Raman") # "Happy Birthday to Raman"

def add(a, b):
  return a + b

add(4,5) # 9

def multiply(x,y):
  return x * y

multiply(5,6) # 30          
```


  |Parameters|Arguments|
  |---|----|
  | A **Parameter** is a variable in method definition| When a method is called, the __arguments__ are the data you pass into the method's parameters|
  |Parameter is a variable in the declaration of function|Argument is the actual value of this variable that gets passed to the function.|

  #### Common Mistakes.

  ```Python
#----1-----
# This mistakes refers to the indentation of the code which messes up the output
def sum_odd(nums):
  total = 0
  for num in numbers:
    if nums % 2 != 0:
      total += num
    return total
# This happens due improper return statement which results in yielding a single value      
sum_odd([1,2,3,4,5,6,7]) # 1
#---Rectification
def sum_odd(nums):
  total = 0
  for num in numbers:
    if nums % 2 != 0:
      total += num
  return total
# The return value should be after the for loop which doesn't mess with normal flow of the code.
sum_odd([1,2,3,4,5,6,7]) # 16

#----2-----    
#Cleaner code - Eliminating Unnecessary else.   
def is_odd(num):
  if num % 2 != 0:
    return False
  else:
    return True

#Can be Written as
def is_odd(num):
  if num % 2 != 0:
    return False
  return True      
```

#### Default Parameter
- Let's Understand the concepts with Examples, comments will be self-explanatory.
- If the number if arguments are not equal to the number of parameters the function breaks. But if we use default parameters, it's value is automatically taken.
- They allow us to be more defensive
- Avoid errors with incorrect parameters.
- More readable examples.

```Python
def exponent(num, power=2):
  return num ** power

print(exponent(2,3)) # 8
print(exponent(4)) # 8

def add(a,b):
  return a + b

add() # doesn't work, nope

def add(a=3, b=7):
  return a + b

add() # 10
# overrriding both the vales.
add(5,6) # 11
add(4) # 11, the position of the arguments matters.
```

- **What can Default Parameters be?**
  - Anything - Functions, lists, dictionary, strings, booleans.

  ```Python
  def add(a,b):
    return a + b

  def math(a,b, fn=add):
    return fn(a, b)

  def sub(a,b):
    return a - b

  math(2,2) # 4
  math(2,3, sub) # -1  
  # Kinda Brain Twister.     
  ```

#### Keyword Arguments.
