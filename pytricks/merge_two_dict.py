#How to merge two dictionaries in 3.5+

x = {'a': 34, 'b': 45}
y= {'b': 78, 'd': 93}

z = {**x, **y}

print(z)


