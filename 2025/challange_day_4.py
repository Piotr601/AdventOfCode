import numpy as np

NUMBER_OF_ROLLS_OF_PAPPER_NEXT = 4
total_rolls = 0
indexes_to_update = []

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
    global indexes_to_update
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
            indexes_to_update.append([row_index,col_index])
    else:
        pass
    
    
def check_numpy_matrix_rolls_of_paper(matrix):
    global total_rolls
    for ind_r, row in enumerate(matrix):
        for ind_c, col in enumerate(row):
            check_for_current_position(matrix, ind_r, ind_c)
    print(total_rolls)

def update_index_list_to_zero(matrix, list_of_index):
    for x,y in list_of_index:
        matrix[x][y] = 0
    
def check_repetative_numpy_matrix_rolls_of_paper(matrix):
    global total_rolls
    global indexes_to_update
    total_rolls = 0
    
    while True:
        indexes_to_update = []
        for ind_r, row in enumerate(matrix):
            for ind_c, col in enumerate(row):
                check_for_current_position(matrix, ind_r, ind_c)
        update_index_list_to_zero(matrix, indexes_to_update)
        if len(indexes_to_update) == 0:
            break
        # store the x_ind and y_ind, at the end replace it and run once again
    print(total_rolls)
    
def main():
    file_input = load_input_file()
    matrix = preprocess_input(file_input)
    check_numpy_matrix_rolls_of_paper(matrix)
    check_repetative_numpy_matrix_rolls_of_paper(matrix)
    
if __name__ == "__main__":
    main()
