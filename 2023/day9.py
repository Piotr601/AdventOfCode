
total_sum = 0
lines = []

def find_next_value(arr):
    val = 0
    while True:
        val += arr[-1]
        differences = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
        arr = differences
        if all(diff == 0 for diff in differences):
            return val       
        
        
def find_previous_value(arr):
    val = 0
    while True:
        differences = [history[i + 1] - history[i] for i in range(len(history) - 1)]
        history = differences
        if all(diff == 0 for diff in differences):
            break
    while True:
        new_values = [history[i] + history[i - 1] for i in range(len(history))]
        history = new_values
        if len(history) == 1:
            return history[0]
        

with open('2023/day9.txt','r') as file:
    for line in file:
        lines.append(list(map(int, line.split())))
        
    next_value = [find_next_value(line) for line in lines]
    previous_value = [find_previous]
    total_sum = sum(next_value)
    print(total_sum)