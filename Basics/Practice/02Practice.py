# some subtle examples of list comphresension and what it is.
# Understanding the format.


# L = [mapping-expression for element for element in soure-list if filter-expression]

powers_of_two = [2**n for n in range(1,7)]
print(powers_of_two)
