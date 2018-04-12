print([i for i in range(20) if i % 3 > 0])
#[1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19]



# Comparison in two types of list creation
# 1. Creating by appending to empty list.
L = []
for n in range(12):
    L.append(n ** 2)
print(L)

# 2. Using List-Comprehension.
p = [n ** 2 for n in range(12)]
print(p)


# A case of multiple iteration.
mi = [(i, j) for i in range(2) for j in range(3)]
print(mi)


# A SET Comprehension WHICH ELIMINATES  DUPLICATES.
setl = {a % 3 for a in range(1000)}
print(setl)
