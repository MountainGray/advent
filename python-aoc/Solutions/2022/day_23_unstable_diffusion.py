from advent import get_input, solution_timer
from collections import defaultdict

around = [(1,0), (1,1), (1,-1), (0,1), (0,-1), (-1,0), (-1,1), (-1,-1)]
moves = [
    [(0,-1), (1,-1), (-1,-1)],  #N
    [(0,1), (1,1), (-1,1)],     #S
    [(-1,0), (-1,1), (-1,-1)],  #W
    [(1,0), (1,1), (1,-1)],     #E
]

@solution_timer(2022, 23, 1)
def part_one(inp):
    elves = {}
    for j, line in enumerate(inp):
        for i, char in enumerate(line):
            if char == "#":
                elves[(i, j)] = -1

    proposal = defaultdict(int)
    for i in range(10):
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
                        proposal[(x+dx, y+dy)] += 1
                        break
        nelfdict = {}
        for elf in elves.keys():
            if elves[elf] != -1:
                if proposal[elves[elf]] == 1:
                    nelf = elves[elf]
                    nelfdict[nelf] = -1
                else:
                    nelfdict[elf] = -1
            else:
                nelfdict[elf] = -1
        elves = nelfdict
        proposal = defaultdict(int)

    keys = elves.keys()
    min_x = min(keys, key=lambda x: x[0])[0]
    max_x = max(keys, key=lambda x: x[0])[0]
    min_y = min(keys, key=lambda x: x[1])[1]
    max_y = max(keys, key=lambda x: x[1])[1]
    ans = 0
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            if (x, y) not in elves:
                ans +=1
    return ans

@solution_timer(2022, 23, 2)
def part_two(inp):
    elves = {}
    for j, line in enumerate(inp):
        for i, char in enumerate(line):
            if char == "#":
                elves[(i, j)] = -1

    proposal = defaultdict(int)
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
                        proposal[(x+dx, y+dy)] += 1
                        break
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
        i+=1
        if not moved:
            break
        proposal = defaultdict(int)
    return i


if __name__ == "__main__":
    input = get_input(2022, 23)
    part_one(input)
    part_two(input)