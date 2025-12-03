
def convert_to_uppercase(rows_list):
    return [elem.upper() for elem in rows_list]

def load_input_file():
    with open('2025/challange_day_1_input.txt', 'r') as file:
        data = file.read().strip().split('\n')
    return data

def load_operation(operation):
    rotate = operation[0]
    rotate_value = int(operation[1:])
    return rotate, rotate_value

def rotate(position, direction, value):
    value = value % 100
    
    if direction == "L":
        position -= value
        
    elif direction == "R":
        position += value
    
    if position < 0:
        position = 100 + position
    elif position > 99:
        position = position - 100
        
    return position

def advanced_rotate(password_counter, position, direction, value):
    password_counter = password_counter + (value // 100)
    value = value % 100

    if direction == "L":
        if position == 0:
            position = 100
        position -= value     
    elif direction == "R":
        if position == 100:
            position = 0
        position += value
    
    if position == 0:
        password_counter += 1
            
    if position < 0:
        position = 100 + position
        password_counter += 1
        
    elif position > 99:
        position = position - 100
        password_counter += 1
        
    return password_counter, position

def main():
    # Loading input file
    file_input = load_input_file()
    input_uppercase = convert_to_uppercase(file_input)
    
    # First part of the challange
    password_counter = 0
    position = 50                   # starting position
    
    for rotate_operation in input_uppercase:
        direction, value = load_operation(rotate_operation)
        position = rotate(position, direction, value)
        
        if position == 0:
            password_counter += 1

    print(f"Password: {password_counter}")

    # Second part of the challange
    position = 50                   # reseting position
    password_counter_advanced = 0
    
    for rotate_operation in input_uppercase:
        direction, value = load_operation(rotate_operation)
        password_counter_advanced, position = advanced_rotate(
            password_counter_advanced, position, direction, value
        )
        
    print(f"Advanced password: {password_counter_advanced}")
    
if __name__ == "__main__":
    main()
