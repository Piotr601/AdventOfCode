import numpy as np

NUMBER_OF_ROLLS_OF_PAPPER_NEXT = 4
total_rolls = 0

def load_input_file():
    with open('2025/challange_day_4_input.txt', 'r') as file:
        data = file.read().strip().split('\n')
    return data

def preprocess_input(data):
    w, h = len(data[0]), len(data)
    
    matrix = np.zeros((w,h), dtype=int)

    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == '@':
                matrix[x][y] = 1
                
    return matrix

def check_next_to_fields(matrix, x, y):
    try:
        if matrix[x][y] == 1 and x>=0 and y>=0:
            return 1
        else:
            return 0
    except IndexError:
        return 0
    
def check_for_current_position(matrix, row_index, col_index):
    global total_rolls
    if matrix[row_index][col_index] == 1:
        next_to_sum = 0
        next_to_sum += check_next_to_fields(matrix, row_index, col_index-1)     # left
        next_to_sum += check_next_to_fields(matrix, row_index, col_index+1)     # right
        
        next_to_sum += check_next_to_fields(matrix, row_index+1, col_index-1)   # top-left
        next_to_sum += check_next_to_fields(matrix, row_index+1, col_index)     # top
        next_to_sum += check_next_to_fields(matrix, row_index+1, col_index+1)   # top-right
        
        next_to_sum += check_next_to_fields(matrix, row_index-1, col_index-1)   # bottom-left
        next_to_sum += check_next_to_fields(matrix, row_index-1, col_index)     # bottom
        next_to_sum += check_next_to_fields(matrix, row_index-1, col_index+1)   # bottom-right
        
        if next_to_sum < NUMBER_OF_ROLLS_OF_PAPPER_NEXT:
            total_rolls += 1
    else:
        pass
    
    
    
def check_numpy_matrix_rolls_of_paper(matrix):
    global total_rolls
    for ind_r, row in enumerate(matrix):
        for ind_c, col in enumerate(row):
            check_for_current_position(matrix, ind_r, ind_c)
            
    print(total_rolls)

def main():
    file_input = load_input_file()
    matrix = preprocess_input(file_input)
    check_numpy_matrix_rolls_of_paper(matrix)    
    
if __name__ == "__main__":
    main()
