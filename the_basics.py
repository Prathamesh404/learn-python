# The If statements,
x = int(input('Enter the integer: '))
if x < 0:
    x = 0
    print("Yeah we changed it to zero")
elif x == 0:
    print('From Zero you need to become Hero')
elif x == 1:
    print("You are one step closer to become a programming")
else:
    print("You got curiosity and Zen, my friend")

#>>>>>>>>>>>>>>
# Notes about if,
#    i. There can be zero or more elif(short for elif) parts & else part is optional.
#    ii. if...elif...elif is basically a substittue to switc or case statements.
# ---------------------------------x---------------------------------------

# 2.for statements.
# Example First, Theory Later.
big_name_poison = ["Vodka", 'Rum', "Absinth", "Beer"]
for w in big_name_poison:
    print(w, len(w))

# The Range Functions:
# To iterate over sequence of numbers, the built-in function 'range()' comes in handy.
# It generates arithmetic progressions:
for i in range(5):
    print(i)

# We can executes the range functions with steps(which can be negative also)

for i range(5, 10): #(x,y) --> x inclusive, exclude y.
    print(i)

for i in range (0, 50, 5):
    print(i)

# Looping through list with 'range()' and 'len()'for iterating over the indices of a sequence.
man_city = ["Aguero", "Silva", "Sane", " Kevin De Bryune"]
for player in range(len(man_city)):
    print(i, a[i])

    
