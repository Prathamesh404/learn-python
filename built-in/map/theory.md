## map()

##### A standard function that accepts at least two arguments, a function and an `iterable`(something that can be iterated over - lists, strings, dictionaries, sets, tuples). It basically run the lambda for each value in the iterable and returns a map object which can be converted into another data structure.

```Python
nums  = [2,4,6,8,10]
doubles = list(map(lambda x:x*2, nums))
print(doubles)
```
