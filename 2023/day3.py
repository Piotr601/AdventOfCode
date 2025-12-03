import re

input_f = open('2023/day3.txt').read().split()

all_sum = 0
numbers = []

for row in input_f:
    nums = re.findall(r'\d+|\D+', row)
    numb = [int(x) for x in nums if x.isdigit()]
    numbers.extend(numb)
    
for i, val in enumerate(input_f):
    pass
    
print(numbers)