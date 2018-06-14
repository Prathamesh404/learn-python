#! /usr/bin/env python3

import statistics

data = [1.3,4.5,6.7,8.9, 4.5]
avg = statistics.mean(data)
b_average = list(filter(lambda x: x < avg, data))
a_average = list(filter(lambda x: x > avg, data))

print("This is below average: ", b_average)
print("This is above average: ", a_average)

