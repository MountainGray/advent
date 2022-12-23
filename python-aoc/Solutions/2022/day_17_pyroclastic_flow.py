from advent import get_input, solution_timer
inp = get_input(2022, 17)[0]
rocks = '''####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##'''.split('\n\n')
rocks = [i.splitlines() for i in rocks]
width = 7


@solution_timer(2022, 17, 1)
def part_one(inp):
    
    positions = set()

    rock_num = 0
    move = 0
    top = -1

    for _ in range(2022):
        fallen = False
        y = top + 4
        x = 2
        rock = rocks[rock_num]
        r_width = len(rock[0])
        r_height = len(rock)
        while not fallen:
            dir = inp[move]
            move = (move+1)%len(inp)
            match dir:
                case ">":
                    if x + r_width < width and not any((x+dx+1, y+dy) in positions for dy in range(r_height) for dx in range(r_width) if rock[~dy][dx] == "#"):
                        x+=1
                case "<":
                    if x > 0 and not any((x+dx-1, y+dy) in positions for dy in range(r_height) for dx in range(r_width) if rock[~dy][dx] == "#"):
                        x-=1

            if y-1>=0 and not any((x+dx, y+dy-1) in positions for dy in range(r_height) for dx in range(r_width) if rock[~dy][dx] == "#"):
                y-=1
            else:
                fallen = True
                for dy in range(r_height):
                    for dx in range(r_width):
                        if rock[~dy][dx] == "#":
                            positions.add((x+dx, y+dy))
        
        top = max(positions, key=lambda x: x[1])[1]
        rock_num = (rock_num+1)%5
    return top +1

@solution_timer(2022, 17, 2)
def part_two(inp):

    positions = set()
    rock_num = 0
    move = 0
    top = -1

    iters= 1_000_000_000_000
    offset = iters - 1729
    presum = (offset//1720)*2738
    remaining = offset%1720
    remaining += 1729

    for _ in range(remaining):
        fallen = False
        y = top + 4
        x = 2
        rock = rocks[rock_num]
        r_width = len(rock[0])
        r_height = len(rock)
        while not fallen:
            dir = inp[move]
            move = (move+1)%len(inp)
            match dir:
                case ">":
                    if x + r_width < width and not any((x+dx+1, y+dy) in positions for dy in range(r_height) for dx in range(r_width) if rock[~dy][dx] == "#"):
                        x+=1
                case "<":
                    if x > 0 and not any((x+dx-1, y+dy) in positions for dy in range(r_height) for dx in range(r_width) if rock[~dy][dx] == "#"):
                        x-=1

            if y-1>=0 and not any((x+dx, y+dy-1) in positions for dy in range(r_height) for dx in range(r_width) if rock[~dy][dx] == "#"):
                y-=1
            else:
                fallen = True
                for dy in range(r_height):
                    for dx in range(r_width):
                        if rock[~dy][dx] == "#":
                            positions.add((x+dx, y+dy))
        
        top = max(positions, key=lambda x: x[1])[1]
        rock_num = (rock_num+1)%5

    return top + presum + 1

if __name__ == "__main__":
    input = get_input(2022, 17)[0]
    part_one(input)
    part_two(input)