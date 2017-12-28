# Given an array , check whether the array is sorted , (With Recursion)

def sort_arr_rec(A):
    # Base case
    if len(A)==1:
        return True
    return A[0]<=A[1] and sort_arr_rec(A[1:]) # We can use slicing.

A = [234, 67, 78, 67, 90, 56]
#print (sort_arr_rec(A))
print(sort_arr_rec(A))

"""
We need to short circuit the whole problem after checking the Base case,
then again we slice the array and try to check the the item at Oth and 1st Position.
if the condition turns true the array keep on slcing till it hit the base case, i.e it only have one element left and thus
giving us a True Solution.
"""
