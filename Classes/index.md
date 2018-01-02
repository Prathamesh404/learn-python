## Classes

> We will be learning how to create and use classes within python and how object-oriented concepts are applied within the classes. Basics of creating and instantiating classes, inheritence in class & instance variables, static methods and class methods.

#### Why we even Classes?
Because they allow us to logically group our data and functions in a way that's easy to _resuse_ asn easy to _build upon_ if need to be. Data and function associated with a specific class are generally referred as attributes and methods. A **Method** is a function associated with a class.


#### Creating and using your own types and classes.

- Creating a Class:
  - defining the class
  - defining class attributes


- Using class involves:
    - Creating new instances of objects.
    - Doing operations on the instances.

#### Defining your own types:
  ```python
    class Footballer(object):
      #define attributes here
  ```
  - This is similar to `def`, indent code to indicate which statements are part of the  _class definition_.
  - the word _object_ means _Footballer_ is a python objects and inherits all its attributes.
    - __Footballer__ is a subclass of an _object_
    - **object** is a superclass of _Footballer_

#### What are Attributes?
Data and procedures that "_belong_" to the classes.

- Data Attributes
  - think of data as other objects that make up the class.


- methods(procedural attributes)
    -  think of methods as functions that only works with the class.
    - how to interact with the object.

#### Defining how to create an instance of a class.
- First have to define __how to create an instance__ of object
- Using a _special_ method `__init__` to initialize some data attributes.

```python
class Coordinate (object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
```
```python
#__init__ - special method to create an instance`
#self - parameter to refer to an instance of the class, its kinda placeholder for any sort of instance when you create an object.
```

#### Actually creating an instance of an class.
- Data attributes of an instance are called instance variables.
- don't provide argument for _self_ , python does this automatically.

```python
c = Coordinate(3,4)
origin = Coordinate(0,0) # create a new object of type "Coordinate" and pass in 3 & 4 to the __init__
print(c.x)
print(origin.x)
```

#### Define a method for the Coordinate Class.
- Other than `self` and dot notation. methods behave just like functions(take params, do operations, return)

```python
class Coordinate(object):
  """docstring for Coordinate."""
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distance(self, other):
    x_diff_sq = (self.x - other.x)**2
    y_diff_sq = (self.y - other.y)**2
    return (x_diff_sq + y_diff_sq)**0.5
```

#### How to use a method
Here how it works

```python
    def distance(self):
      # Code goes Here
    ```      

Using a class:
- Conventional way
   ```python
   c = Coordinate(3,4)
   zero = Coordinate(0,0)
   print(c.distance(zero))
   # c - object to call method on.
   # distance - name of method
   # zero - parameters not including self (self is implied as c)
   ```
- And the equivalent to the above, with breakdown.
  ```python
    c = Coordinate(3,4)
    zero = Coordinate(0,0)
    print(Coordinate.distance(c,zero))
    #Coordinate - name of class
    # distance - name of method
    # (c,zero) - parameters, including an object to call the method on representing self.
    ```
