from tqdm import tqdm
import numpy as np
from itertools import chain

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
    
    
def get_fresh_indegriends_ids(file_input):
    fresh_product_ranges = [item for item in file_input if '-' in item]
    ranges = []
    fresh_product_ranges.sort()
    for product_range in fresh_product_ranges:
        range_start, range_end = product_range.split('-')
        ranges.append(range(int(range_start), int(range_end)+1))

    flat_ranges = set(list(chain.from_iterable(ranges)))    # this us causing memory error
    print(len(flat_ranges))                                 # TODO Find a different way to calculate it
    
def main():
    file_input = load_input_file()
    get_indegriends_ids(file_input)
    get_fresh_indegriends_ids(file_input)
    
if __name__ == "__main__":
    main()
