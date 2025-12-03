
import numpy as np

bag_r = 12
bag_g = 13
bag_b = 14

# 2.1
def check_game_is_valid(game):

    items = game.split(',')
    for ite in items:
        i = ite.strip().split()
        #print(i, ite)
        if i[1] == 'blue':
            if int(i[0]) > bag_b: 
                return 0

        elif i[1] == 'red':
            if int(i[0]) > bag_r: 
                return 0
            
        elif i[1] == 'green':
            if int(i[0]) > bag_g: 
                return 0

        
# 2.2
def check_fewest_valid_game(r,g,b,game):
    print(r,g,b, game)
    items = game.split(',')
    for ite in items:
        i = ite.strip().split()
        if i[1] == 'red':
            r = max(r, int(i[0]))
        if i[1] == 'green':
            g = max(g, int(i[0]))
        if i[1] == 'blue':
            b = max(b, int(i[0]))
    return r,g,b
        
with open('2023/day2.txt','r') as file:
    #s1 = 0
    s2 = 0
    
    for line in file:
        g_res = []
        
        line = line.strip().replace(':', ';')
        l_split = line.split(';')
        
        id = int(l_split[0][5:])

        min_r, min_g, min_b = 0, 0, 0
        
        for games in l_split[1:]:
            # g_res.append(check_game_is_valid(games))
            min_r, min_g, min_b = check_fewest_valid_game(min_r, min_g, min_b, games)

        s2 += (min_r * min_g * min_b)

        # if all([x == None for x in g_res]):
        #     s1 += id
        
    print(s2)
