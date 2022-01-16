inp = open('2021/day25/input.txt').read().split('\n')
from copy import deepcopy
pos = [[i for i in line] for line in inp]
width = len(pos[0])
height = len(pos)

changed = True
l = 0
while changed:
    l +=1
    changed = False
    new = deepcopy(pos)

    #left
    for j in range(len(inp)):
        for i in range(len(inp[0])):
            if pos[j][i] == ">":
                if pos[j][(i+1)%width] == ".":
                    new[j][(i+1)%width] = ">"
                    new[j][i] = "."
                    changed= True
    pos = new
    new = deepcopy(pos)

    for j in range(len(inp)):
        for i in range(len(inp[0])):
            if pos[j][i] == "v":
                if pos[(j+1)%height][i] == ".":
                    new[(j+1)%height][i] = "v"
                    new[j][i] = "."
                    changed= True
    pos = new
    
    for k in pos:
        print(k)
    print()

    
print(l)




