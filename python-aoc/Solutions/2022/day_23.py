from advent import get_input
inp = get_input(2022, 23)
# defaultdict
from collections import defaultdict
elves = {}



# all 8 directions
around = [(1,0), (1,1), (1,-1), (0,1), (0,-1), (-1,0), (-1,1), (-1,-1)]
moves = [
    [(0,-1), (1,-1), (-1,-1)], #N
    [(0,1), (1,1), (-1,1)], #S
    [(-1,0), (-1,1), (-1,-1)], #W
    [(1,0), (1,1), (1,-1)], #E
]

for j, line in enumerate(inp):
    for i, char in enumerate(line):
        if char == "#":
            elves[(i, j)] = -1

rounds = 10
proposal = {}
i=0
while True:
    for elf in elves.keys():
        move = False
        x, y = elf
        for dx, dy in around:
            if (x+dx, y+dy) in elves:
                move = True
                break
        if move:
            for j in range(4):
                empty = True
                for dx, dy in moves[(i+j)%4]:
                    if (x+dx, y+dy) in elves:
                        empty = False
                        break
                if empty:

                    dx, dy = moves[(i+j)%4][0]
                    elves[elf] = (x+dx, y+dy)
                    if (x+dx, y+dy) in proposal:
                        proposal[(x+dx, y+dy)] += 1
                    else:
                        proposal[(x+dx, y+dy)] = 1
                    break
    # move elves that only want one space
    nelfdict = {}
    moved = False
    for elf in elves.keys():
        if elves[elf] != -1:
            if proposal[elves[elf]] == 1:
                moved = True
                nelf = elves[elf]
                nelfdict[nelf] = -1
            else:
                nelfdict[elf] = -1
        else:
            nelfdict[elf] = -1
    elves = nelfdict
    if not moved:
        break
    else: i+=1
    # reset proposal
    proposal = {}

                    
#keys = elves.keys()
#min_x = min(keys, key=lambda x: x[0])[0]
#max_x = max(keys, key=lambda x: x[0])[0]
#min_y = min(keys, key=lambda x: x[1])[1]
#max_y = max(keys, key=lambda x: x[1])[1]

# get size of rectangle
#print(min_x, max_x, min_y, max_y)
#print((max_x-min_x)*(max_y-min_y))
#ans = 0
#for x in range(min_x, max_x+1):
    #for y in range(min_y, max_y+1):
        #if (x, y) not in elves:
            #ans +=1
#print(ans)
print(i)

        


    # part 1



