import numpy as np


def part_one():
    with open("2022/day_3.txt") as file:
        for line in file:
            l = line.split()
            l_i = l[0]
            
            for letter in set(l_i):
                print(l_i.count(letter))
                
                
            print(l_i)
            
part_one()