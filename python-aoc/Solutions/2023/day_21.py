from advent import get_input, solution_timer
from advent.helpers import grid_8_neigbours


@solution_timer(2023, 21, 1)
def part_one(inp):
    inp = [[i for i in line] for line in inp]
    mx, my = len(inp[0]), len(inp)
    sx, sy = (mx//2, my//2)
    inp[sy][sx] = "."
    cpos = set([(sx,sy)])

    steps = 64 
    while steps > 0:
        steps -= 1
        npos = set()
        for pos in cpos:
            for n in grid_8_neigbours(pos):
                nx, ny = n
                if 0 <= nx < len(inp[0]) and 0 <= ny < len(inp):
                    if inp[ny][nx] != "#" and n not in cpos:
                        npos.add(n)
        cpos = npos
    return len(cpos)


def grid_8_neigbours(pos):
    i, j = pos
    for y in range(-1, 2):
        for x in range(-1, +2):
            if x == 0 or y == 0 and x != y:
                yield (i+x, j+y)




@solution_timer(2023, 21, 2)
def part_two(inp, steps = 26501365):
    inp = [[i for i in line] for line in inp]
    mx, my = len(inp[0]), len(inp)
    sx, sy = (mx//2, my//2)
    inp[sy][sx] = "."
    cpos = set([(sx, sy)])
    bpos = cpos
    rem = steps % 2
    tot = 1 if rem == 0 else 0
    ptot = 0
    pdelt = 0
    ptot = 0
    i = 0
    predict = 0
    while i < steps:

        i += 1
        npos = set()
        for pos in bpos:
            for n in grid_8_neigbours(pos):
                nx, ny = n
                if inp[ny%my][nx%mx] != "#":
                    if n not in cpos and n not in npos:
                        npos.add(n)
                        if i % 2 == rem:
                            tot += 1
            
        cpos = bpos
        bpos = npos

        if (i-(mx//2)) % (mx*2) == 0:
            delt = tot - ptot
            acel = delt - pdelt
            ptot = tot
            pdelt = delt
            if tot - predict == 0:
                while i < steps:
                    i += mx*2
                    delt += acel 
                    tot += delt 
                return tot
            predict = tot + delt + acel
            
    return tot


if __name__ == "__main__":
    inp = get_input(2023, 21)
    part_one(inp)
    part_two(inp)
