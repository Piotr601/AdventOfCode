import numpy as np

sum = 0
max_sum = 0

with open('2022/day_1.txt','r') as file:
    for line in file:
        if not line.isspace():
            sum += int(line)
        else:
            max_sum = max(sum, max_sum)
            sum = 0
            
print(max_sum)