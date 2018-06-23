import re
x = "From: all the things : this"
y = re.findall('^F.+:', x)
print(x)
print(y) # ["From: all the things :"]
