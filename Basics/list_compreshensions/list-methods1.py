# We will be learing methods of list which are useful while coding.
# Method1 (append)
fruits = ["mango","watermelon","guava","grapes","litchi"]
fruits.append ("muskmelon")
print("New list is",fruits)
# ['mango', 'watermelon', 'guava', 'grapes', 'litchi', 'muskmelon']
# Method2 (extend)
newfruits = ["apple","apricot","banana"]
fruits.extend(newfruits)
print("Fruits list",fruits)
#['mango', 'watermelon', 'guava', 'grapes', 'litchi', 'muskmelon', 'apple', 'apricot', 'banana']
# Method3 (insert)
fruits.insert(4,"bluebeery")
print("newfruits1",fruits)
#['mango', 'watermelon', 'guava', 'grapes', 'bluebeery', 'litchi', 'muskmelon', 'apple', 'apricot', 'banana']
# Method4 (Remove)
fruits.remove("watermelon")
print("fruitlist2",fruits)
#['mango', 'guava', 'grapes', 'bluebeery', 'litchi', 'muskmelon', 'apple', 'apricot', 'banana']
#Method5 (index)
index = fruits.index("grapes")[]

print("index of grapes",index)
#index of grapes 2
# Method5 (slice)
print(fruits[2:5])
# this will print the list in between of 2 and 5
#['grapes', 'bluebeery', 'litchi']
#Method6 (len)
print("The length of the list is",len(fruits))
#this will print the length of the list.
#The length of the list is 9
# Metho7(clear)
fruits.clear()
print(fruits)
#this clears all the elements of the list
#[]
