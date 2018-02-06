# Generate a list of candidates
L = [n for n in range(2, 40)]
print(L)

# Remove all multiples of the first value
L = [n for n in L if n == L[0] or n % L[0] > 0]
print(L)

# Remove all multiples of the second value
L = [n for n in L if n == L[1] or n % L[1] > 0]
print(L)

# Remove all multiples of the third value
L = [n for n in L if n == L[2] or n % L[2] > 0]
print(L)
