from datetime import date
from datetime import time
from datetime import datetime

ticks = time.time()
print("Number of ticks since epoch: ",ticks)

localtime = time.localtime(time.time())
print("local current time is: ", localtime)


