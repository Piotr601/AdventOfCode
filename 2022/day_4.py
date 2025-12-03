import string

def part_one():
    
    with open("2022/day_4.txt") as file:
        for line in file:
            l = line.split("\n")[0].split(",")
            arr_fp, arr_sp = [], []
            
            # first person, second person
            fp, sp = l[0].split("-"), l[1].split("-")
            
            print(fp, sp)
            
    # for item in range(int(len(arr_fp))):
    #     if arr_fp[item] in arr_sp[item] or arr_sp[item] in arr_fp[item]:
    #         print(item)

def part_two():
    pass

part_one()
#part_two()