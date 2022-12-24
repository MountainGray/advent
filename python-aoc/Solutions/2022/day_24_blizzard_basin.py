from advent import get_input, solution_timer
from collections import defaultdict
inp = get_input(2022, 24)

min_x, max_x = 0, len(inp[0]) -1
min_y, max_y = 0, len(inp) -1
start, end = (1,0), (max_x-1, max_y)

def parse_inp(inp):
    blizards = set()
    for j, line in enumerate(inp):
        for i, char in enumerate(line):
            match char:
                case ">": blizards.add((i, j, 1, 0))
                case "<": blizards.add((i, j, -1, 0))
                case "^": blizards.add((i, j, 0, -1))
                case "v": blizards.add((i, j, 0, 1))
    return blizards


def move_blizards(blizards):
    new_blizards = set()
    for x, y, dx, dy in blizards:
        if x + dx == min_x: new_blizards.add((max_x-1, y+dy, dx, dy))
        elif x + dx == max_x: new_blizards.add((min_x+1, y+dy, dx, dy))
        elif y + dy == min_y: new_blizards.add((x+dx, max_y-1, dx, dy))
        elif y + dy == max_y: new_blizards.add((x+dx, min_y+1, dx, dy))
        else: new_blizards.add((x+dx, y+dy, dx, dy))
    return new_blizards
            
def traverse_blizzard(blizards, start, end):
    fan = {start}
    ans = 0
    while True:
        new_fans = set()
        if end in fan: break
        ans += 1

        blizards = move_blizards(blizards)
        taken = defaultdict(int)
        for x,y, _, _ in blizards:
            taken[(x,y)] += 1

        for x, y in fan:
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1), (0,0)]:
                if ((x+dx) <max_x and (y+dy) < max_y and (x+dx) > min_x and (y+dy) > min_y) or ((x+dx, y+dy) == end) or ((x+dx, y+dy) == start):
                    if (x+dx, y+dy) not in taken:
                        new_fans.add((x+dx, y+dy))
        fan = new_fans
    return blizards, ans
                        
@solution_timer(2022, 24, 1)
def part_one(inp):
    blizards = parse_inp(inp)
    blizards, ans = traverse_blizzard(blizards, start, end)
    return ans

@solution_timer(2022, 24, 2)
def part_two(inp):
    blizards = parse_inp(inp)
    blizards, ans = traverse_blizzard(blizards, start, end)
    blizards, ans2 = traverse_blizzard(blizards, end, start)
    blizards, ans3 = traverse_blizzard(blizards, start, end)
    return ans+ans2+ans3


if __name__ == "__main__":
    input = get_input(2022, 24)
    part_one(input)
    part_two(input)