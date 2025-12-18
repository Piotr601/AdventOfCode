from tqdm import tqdm
import numpy as np

def load_input_file():
    with open('2025/challange_day_5_input.txt', 'r') as file:
        data = file.read().strip().split('\n')
    return data

def get_indegriends_ids(file_input):
    fresh_product_ids = []
    fresh_product_ranges = [item for item in file_input if '-' in item]
    product_ids_to_check = [int(item) for item in file_input if '-' not in item and len(item) > 0]
    
    for product_id in product_ids_to_check:
        for product_range in fresh_product_ranges:
            range_start, range_end = product_range.split('-')
            if product_id in range(int(range_start), int(range_end)+1):
                fresh_product_ids.append(product_id)
        
    unique_products_ids = list(set(fresh_product_ids))
    print(len(unique_products_ids))
    
    
def main():
    file_input = load_input_file()
    get_indegriends_ids(file_input)
    
if __name__ == "__main__":
    main()
