from tqdm import tqdm
import numpy as np

def load_input_file():
    with open('2025/challange_day_6_input.txt', 'r') as file:
        data = file.read().strip().split('\n')
    return data

def calculate_math_homework(file_input):
    file_input = [row.split() for row in file_input[::-1]]
    
    matrix = np.array(file_input)
    matrix = np.rot90(matrix)
    number_sum = 0
    
    for row in matrix:
        operator = ""
        number = 0
        for w in range(0, len(row)):
            if w == 0:
                operator = row[w]
            elif w == 1:
                number = int(row[w])
            else:
                match operator:
                    case '+':
                        number += int(row[w])
                    case '*':
                        number *= int(row[w])
        number_sum += number
    print(number_sum)
        

def main():
    file_input = load_input_file()
    calculate_math_homework(file_input)
    
if __name__ == "__main__":
    main()
