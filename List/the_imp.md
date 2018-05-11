# List Data Structure in Python.

List is the most versatile  _compound_ data type(use to group together different values) in __Python__. Might contain different data types, usually same.

```python
squares = [1,4,9,16,25]
print(squares) #[1,4,9,16,25]
squares[0] # indexing returns respective item.
squares[-1] # negative used for accessing through last element.
#Slicing- it generally return new string,
squares[3:] # [16,25]
# A shallow copy creation.
squares[:] # [1,4,9,16,25]
```
- **append** : _list.append_(x)
 - Add an item to the end of the list. Equivalent to `a[len(a): ] = [x]`
- **extend** : _list.extend_(L)
  - Extend the list by appending all the items in the given list. Equivalent to `a[len(a):] = L`
- **insert** : _list.insert_(i, x)
  - insert an item at an given position. (i -->_index before we want to insert_, x --> _element to insert_). `a.insert(len(a),x) => a.append(x)`
- **remove** : _list.remove(x)_
  - removes first item from the list whose value is x. It is an error if there is no such item.
- **pop** : _list.pop([i])_
  - Removes the item from specific position & return it. No index specified, a.pop() removes and returns the last item in the list.
- **clear** : _list.clear()_
  - Removes all the elements from list. Equivalent to `del a[:]`
- **sort** : _list.sort()_
  - Sort the items of the list **_in place_**.
- **reverse**: _list.reverse()_
  - Reverse the elements of the list in place.
- **copy** : _list.copy_()
  -  Return a shallow copy of the list Equivalent to `a[:]`

```Python
# A big fat list of examples to understand the concepts more deeply.
a = [89, 79, 69, 78.4, 34.5, 69]
print(a.count(69), a.count(34.5), a.count(14))  # 2 1 0
a.insert(2, -1)
a.append(345)
print(a) # [89, 79, -1, 69, 78.4, 34.5, 69, 345]
print(a.index(79)) # 1
a.remove(69)
print(a) # [89, 79, -1, 78.4, 34.5, 69, 345]
print(a.reverse()) # [345, 69, 34.5, 78.4, -1, 79, 89]
print(a.sort()) #[-1, 34.5, 69, 78.4, 79, 89, 345]
```  

### Let's use list as Stacks.
> The list methods make it easy to use a list as a stack, where the last element added is the first element retrieved("Last-In-First-Out" - LIFO). Adding element at top or end of the list with `append()` and removing the last added with `pop()` without an explicit index.

```Python
#Diving into the Code -> Examples are gut..i mean good.
stacky = ["thy", "high", "five"]
stacky.append("lie")
stacky.append("die")
print(stacky) # ["thy", "high", "five","lie","die"]
stacky.pop() # "die", it basically returns the value
print(stacky) # ["thy", "high", "five","lie"]
```
### Let's use list as Queue
> While append and pop at the end of the list are faster, the same at the beginning is slow due to shifting of each element by one. We need faster First-In-First-Out(FIFO) operations.
Special module - `collections.deque`

```Python
from collections import deque
queue =  deque(["Sergio", "Silve", "Sane"])
queue.append("Kevin") # Kevin in the team
queue.append("Bernardo") #Here comes Bernardo
queue.popleft() #First to arrive is gone, goodbye Sergio.
queue.popleft() #Second to arrive is gone too, goodbye Silva.
print(queue) # ["Sane", "Kevin", "Bernardo"]
```

### List Comprehensions
Most concise way to make Lists

```Python
#Normal
squares = []
for x in range(10):
  square.append(x**2)

#Lambda
squares = list(map(lambda x: x**2, range(10)))

#Heroic Pythonic
squares = [x**2 for x in range(10)]  
```
