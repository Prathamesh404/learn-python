# In this program we will try to create a transpose of given matrix, with more code readability and less lines of codes.

# 1.Method One- Using nested-list-comprehensions.
# Nested list comprehensions are used to iterate through each element in the matrix. 
m = [[2,3],[4,5],[7,8]]
for row in m:
    print(row)

m_trans = [m[j][i] for j in range(len(m)) for i in range(len(m[0]))]
for row in m_trans:
    print(row)

# Using 'zip' method: Zip returns a iteraor of tuple contains the ith element form each of the argument sequences or iterable. Unzip the array using *, then zip it to get the transpose.

matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for row in matrix:
    print(row)
print("\n")
t_matrix = zip(*matrix)
for row in t_matrix:
    print(row)
