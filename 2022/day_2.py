'''
    A - rock, B - paper, C - scissors
    Y - paper, X - rock, Z - scissors
    
    6 pts - win, 3 pts - tie, 0 pts - lose
    2 pts - paper, 1 pts - rock, 3 pts - scissors
'''

total_score = 0

# First part
def part_one(total_score):

    with open('2022/day_2.txt','r') as file:
        for line in file:
            line_arr = line.split()
            # print(line_arr)
            
            # Points for winning/drawing
            if line_arr[0] == 'A' and line_arr[1] == 'X' or line_arr[0] == 'C' and line_arr[1] == 'Z'  or line_arr[0] == 'B' and line_arr[1] == 'Y':
                total_score += 3
            # only winning points
            elif line_arr[0] == 'A' and line_arr[1] == 'Y' or line_arr[0] == 'C' and line_arr[1] == 'X'  or line_arr[0] == 'B' and line_arr[1] == 'Z':
                total_score += 6
                
            # Points for picking sth
            if line_arr[1] == 'Y':
                total_score += 2
            elif line_arr[1] == 'X':
                total_score += 1
            else:
                total_score += 3
                
    print(total_score)
    
# Sedond part   
def part_two(total_score):

    with open('2022/day_2.txt','r') as file:
        for line in file:
            line_arr = line.split()
            # print(line_arr)
            
            # Draw
            if line_arr[1] == 'Y':
                if line_arr[0] == 'A':
                    total_score += 1
                elif line_arr[0] == 'B':
                    total_score += 2
                else:
                    total_score += 3
                total_score += 3
            # Lose
            elif line_arr[1] == 'X':
                if line_arr[0] == 'A':
                    total_score += 3
                elif line_arr[0] == 'B':
                    total_score += 1
                else:
                    total_score += 2
            # Win
            else:
                if line_arr[0] == 'A':
                    total_score += 2
                elif line_arr[0] == 'B':
                    total_score += 3
                else:
                    total_score += 1
                total_score += 6
            
                
    print(total_score)
    
part_two(total_score)