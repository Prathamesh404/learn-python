# Python
According to Guido Van Rossum
> high-level programming language, and its core design philosophy is all about code readability and a syntax which allows programmers to express concepts in a few lines.


What most people feel about it,
> Beautiful, like an executable pseudocode, easy to learn, varied applications ranging from Web Development, Data Science & Machine Learning.

#### 1. Variables:
 Words/Phrases that act as a container to store values.

  ```Python
      #Number
      uno = 1

      #Strings
      two = "twice"

      #Booleans
      is_happy = True
      is_dumb = False

      #Float
      milk_price = 21.50
    ```

#### 2. Control Flow & Conditional Statements.
  **If** statement is used to evaluate whether a statement is True of False. The execution of program inside _if_ statement depends on the condition.

  ```Python
  # Only if
  if True:
    print("This is python & it is easy")

  if (34 > 17):
    print("This seem legit math with Bool")

  ```  
  ```python
  #if-else
  if (1 > 2):
    print("Something isn't right")
  else:
    print("Naah, that ain't possible")  

  ```

  ```Python
  #now with some elif
  if (45 < 25):
    print("This ain't Happening")
  elif(45 > 25):
    print("Yeah, now you know how to count")
  else:
    print("What???")    
  ```

#### 3. Lets Loop _for_ a  _while_ and _iterate_
 We generally used _while_ and _for_ loop for iterating

  ```Python
  #the classic print till 10
  #The while loop approach
  number = 1
  while num <= 10:
    print(num)
    num += 1

  condition = True
  while condition:
    print("This is set to {}".format(condition))  
  ```
  ```Python
  #The For loop, with range function things get more easier
  #prints from 1 to 10,
  #it actually avoid the last index
  #and take the penultimate as last argument.
  for i in range(1,11):
    print(i)

  ```

### Lists
Lists are the vital and frequently used _Data Structure_.It's highly versatile and widely popular(also known as _array_ in other programming languages.)

  ```Python
  # empty list
  thy_list = []
  thy_list1 = list()

  #List of numbers(int)
  num_list = [23, 56, 89]

  # The mixed List
  mix_list = ["Seven", 8, "Nine", 10.4]

  print(num_list[0]) # => 23
  print(mix_list[1]) # => 8

  #The append method
  books = []
  books.append("Python for Dummies")
  books.append("Cracking the Coding Interview")

  print(books) #=> ["Python for Dummies", "Cracking the Coding Interview"]
  books[0] #=> "Python for Dummies"
  ```

### Dictionary - key/value pair.
An unordered collection of items. While Other data structue have only value, dictionary comes with _key:value_ pair.

```Python
#A Typical Python Dictionary  
players = {
  "no1": "Sergio Aguero",
  "no2": "David Silva",
  "no3": "Jesus Gabriel"
}   

print("The Striker of Man City is %s" %(players["no1"]))
print("The Magician of Man City is {}".format(players["no2"]))
print("The Younger Talent of Man City is {}".format(players["no3"]))

players["no4"] = "Vincent Kompany"
```

### Iteration

```Python
#Through list
places = ["Rome", "Italy", "Switzerland", "Alps"]
for place in places:
  print(place)
#"Rome"
# "Italy"
# "Switzerland"
#  "Alps"

#Through Dictionary
attributes = {
  "name": "Raven",
  "age": 12,
  "Color": "Black"
  "Sing": False
}

#1 Print the keys and accordingly values
for key in attributes:
  print("{0} ---> {1}".format(key, attributes[key]))
# name ---> Raven
# age ---> 12
# Color ---> Black
# Sing ---> False


#2 Use the iteritems() method
for key, value in attributes.items():
  print(key, "--->",  value) #same result.

```
### Objects and Classes

- **Objects represents real world scenarios or more implicitly objects that surround us such as car, laptop, mobile.**
- We generally build objects are specify their uniqueness or similarity through the **Data** and their **Characteristics**
- Now we map **Data ---> Attributes** _&&&_ **Characteristics/Behaviour ----> Methods**. This is general consideration in _Object Oriented Programming_.

  #### Classes
  - A _Class_ is a Blueprint, a model for it's object. A class is prototype of the object, e.g. Air Conditioner. It possess details such as type, color, capacity, made, model etc.
  - Now an Object is called an instance of class, and we create a object from the class through _instantiation_.
  - Let's get out hand's dirty by creating some.

    ```Python
    class House:
      pass

      my_house = House()
      print(my_house) #=> <__main__.House instance at 0x7fb651ae56>
      ```
  - Creating a more detailed Class
  ```Python
  class Car():
    """ Let's model a Car."""
    def __init__(self, make, model, year):
      """ Initialize Car Attributes"""
      self.make = make
      self.model = model
      self.year = year
```
