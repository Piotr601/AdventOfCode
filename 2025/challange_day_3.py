def load_input_file():
    with open('2025/challange_day_3_input.txt', 'r') as file:
        data = file.read().strip().split('\n')
    return data

def calculate_two_batteries_bank_joltage(bank):
    first_battery = max(bank[:len(bank)-1])
    first_battery_index = bank.index(first_battery)
    
    sub_bank = bank[first_battery_index+1:]
    second_battery = max(sub_bank)
    
    joltage = first_battery + second_battery
    return int(joltage)

def calculate_complex_bank_joltage(bank):
    joltage = 0
    return int(joltage)

def main():
    banks_input = load_input_file()
    
    produced_joltage = 0
    complex_produced_joltage = 0
    
    for bank in banks_input:
        produced_joltage += calculate_two_batteries_bank_joltage(bank)
        complex_produced_joltage = calculate_complex_bank_joltage(bank)
        
    print(f"Produced joltage: {produced_joltage}")
    print(f"Complex produced joltage: {complex_produced_joltage}")
    
if __name__ == "__main__":
    main()
