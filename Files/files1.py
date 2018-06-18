#! /usr/bin/env python3
# Reading from the file


#1---- Reading the entire file at once
filename = 'learn.txt'

with open(filename) as f_obj:
    contents = f_obj.read()

print(contents)



#2--- Reading line by line
filename = 'learn.txt'

with open(filename) as f_obj:
    for line in f_obj:
        print(line.rstrip())

#3 -- Storing the lines in the list

filename = 'learn.txt'
with open(filename) as f:
    lines = f_obj.readlines()

for line in lines:
    print(line)

# Writing to the file.

filename = 'progr=.txt'
with open(filename, 'w') as f:
    f.write("Always Be Coding")

#Writinng mutiple lines
filename = 'prog.txt'
with open(filename, 'w') as f:
    f.write("Always be coding \n")
    f.write("Never Stop\n")

#appending to the file
filename = 'prog.txt'
with open(filename, 'a') as f:
    f.write("This is tough\n")
    f.write("But equally essential\n")

     
