import numpy as np

sum = 0
max_sum = 0

def part_one(sum, max_sum):
    with open('2022/day_1.txt','r') as file:
        for line in file:
            if not line.isspace():
                sum += int(line)
            else:
                max_sum = max(sum, max_sum)
                sum = 0
                
    print(max_sum)

def part_two(sum, max_sum):
    arr = []
    with open('2022/day_1.txt','r') as file:
        for line in file:
            if not line.isspace():
                sum += int(line)
            else:
                arr.append(sum)
                sum = 0
                
    arr.sort()
    print(np.sum(arr[-3:]))

part_two(sum,max_sum)
