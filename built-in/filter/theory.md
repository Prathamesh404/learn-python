### filter()

#### There is a lambda value for each value in the iterable. It returns filter object which can be converted into other iterables. The object contains only the values that return true to the lambda.

```Python
l = [11, 22, 33, 44, 55, 66, 77]
evens = list(filter(lambda x:x % 2 == 0, l))
print(evens) # [22, 44, 66

```
