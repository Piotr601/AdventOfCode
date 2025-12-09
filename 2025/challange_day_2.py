invalid_id_sum = 0
complex_invalid_is_sum = 0

def load_input_file():
    with open('2025/challange_day_2_input.txt', 'r') as file:
        data = file.read().strip().split(',')
    return data

def convert_to_range(data_entry):
    first_id, last_id = data_entry.split('-')
    id_range = range(int(first_id), int(last_id)+1)
    return id_range

def check_if_number_is_repeated_twice(val, int_length):
    global invalid_id_sum
    first_part = str(val)[:int_length//2]
    second_part = str(val)[int_length//2:int_length]
    if first_part == second_part:
        invalid_id_sum += val

def check_id_range(id_range):
    for val in id_range:
        int_length = len(str(val))
        if int_length % 2 == 0:
            check_if_number_is_repeated_twice(val, int_length)

def split_string(string, split_string):
    return [string[i:i+split_string] for i in range(0, len(string), split_string)]
     
def check_if_number_is_repeated(val, int_length):
    global complex_invalid_is_sum
    for digit_factor in range(1, (int_length//2)+1):
        if int_length % digit_factor == 0:
            splited_string_list = split_string(str(val), digit_factor)
            
            if len(list(set(splited_string_list)))== 1:
                complex_invalid_is_sum += val
                break
        

def check_complex_id_range(id_range):
    for val in id_range:
        check_if_number_is_repeated(val, len(str(val)))
        
def main():
    file_input = load_input_file()

    for entry in file_input:
        id_range = convert_to_range(entry)
        check_id_range(id_range)
        check_complex_id_range(id_range)
        
    print('\n*------------------ RESULTS ------------------*')
    print(f"   Invalid id sum: \t\t{invalid_id_sum}")
    print(f"   Complex invalid id sum:\t{complex_invalid_is_sum}")
    print('*---------------------------------------------*')
if __name__ == "__main__":
    main()
