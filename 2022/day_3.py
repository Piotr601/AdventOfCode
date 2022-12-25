import numpy as np
import string

summator = 0

def part_one(summator):
    with open("2022/day_3.txt") as file:
        for line in file:
            l = line.split()
            l_i = l[0]
            
            mid = int(len(l_i)/2)
            left = l_i[mid:]
            right = l_i[:mid]
            #print(len(left), len(right), left, right)
            
            for letter in set(left):
                if letter in right:
                    
                    temp = letter.islower()
                    # ASCII 97-122 (lower char)
                    if temp:
                        print('lower ', letter, ord(letter))
                        summator += ord(letter) - 96
                    # ASCII 65-90 (upper char)
                    else:
                        print('upper ', letter, ord(letter))
                        summator += ord(letter) - 65 + 27
                    break
    
    print(summator)
              
                
def part_two(summator):
    with open("2022/day_3.txt") as file:
        for line in file:
            l = line.split()
            
            word1 = l[0]
            word2 = file.readline()
            word3 = file.readline()
            
            print(word1, word2, word3)
            #print(l_i)
            #print(len(left), len(right), left, right)
            
            for letter in set(word1):
                if letter in word2 and letter in word3:
                    
                    temp = letter.islower()
                    # ASCII 97-122 (lower char)
                    if temp:
                        print('lower ', letter, ord(letter))
                        summator += ord(letter) - 96
                    # ASCII 65-90 (upper char)
                    else:
                        print('upper ', letter, ord(letter))
                        summator += ord(letter) - 65 + 27
                    break
    
    print(summator)               
            
part_two(summator)        
#part_one(summator)