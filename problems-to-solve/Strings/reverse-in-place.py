#This program works withrversing the string in-place
# This program also converts the string into list first.
# We swap the first and last characters, then the second and second-to-last characters, and so on until we reach the middle.

def reverse(stringo):
    stringo_list = list(stringo)

    left_pointer = 0
    right_pointer = len(stringo_list) -  1

    while left_pointer < right_pointer:

    #Swap characters.
        stringo_list[left_pointer] , stringo_list[right_pointer] = \
         stringo_list[right_pointer], stringo_list[left_pointer]


    # Move towards middle
        left_pointer += 1
        right_pointer -=1

    return ''.join(stringo_list)
