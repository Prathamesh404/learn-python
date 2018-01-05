# Writing a python program that takes two lists and returns true if they have atleat
# one common member.

def common_data(l1, l2):
    result = False
    for x in l1:
        for y in l2:
            if x == y:
                result = True
                return result


print(common_data([2,3,7, 8,0], [4,8,7,2,7,9]))
