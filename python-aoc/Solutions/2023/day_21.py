from advent import get_input, solution_timer, submit
from advent.helpers import *


@solution_timer(2023, 21, 1)
def part_one(inp):

    inp = [[i for i in line] for line in inp]
    for i in inp:
        print(i)
    for idy, line in enumerate(inp):
        for idx, char in enumerate(line):
            if char == "S":
                start = (idx, idy)
                break
    
    sx, sy = start
    inp[sy][sx] = "."
    cpos = set([start])
    print(start)

    steps = 64 
    while steps > 0:
        steps -= 1
        npos = set()
        for pos in cpos:
            for n in grid_ud_neigbours(pos):
                nx, ny = n
                if 0 <= nx < len(inp[0]) and 0 <= ny < len(inp):
                    if inp[ny][nx] != "#" and n not in cpos:
                        print(n, inp[ny][nx])
                        npos.add(n)
        cpos = npos
    return len(cpos)


def grid_udlr_neigbours(pos):
    i, j = pos
    for y in range(-1, 2):
        for x in range(-1, +2):
            if x == 0 or y == 0 and x != y:
                yield (i+x, j+y)




@solution_timer(2023, 21, 2)
def part_two(inp, steps = 26501365):
    inp = [[i for i in line] for line in inp]
    mx, my = len(inp[0]), len(inp)
    pvs = []
    for idy, line in enumerate(inp):
        for idx, char in enumerate(line):
            if char == "S":
                start = (idx, idy)
                break
    
    sx, sy = start
    inp[sy][sx] = "."
    cpos = set([start])
    bpos = cpos
    #bpos |= cpos
    #steps = 100
    #steps = 26501365
    rem = steps % 2
    tot = 1 if rem==0 else 0
    ptot = 0
    pdelt = 0
    ptot = 0
    i = 0
    pacel = 0
    predict = 0
    pdd= 0
    while i < steps:

        i += 1
        npos = set()
        for pos in bpos:
            for n in grid_ud_neigbours(pos):
                nx, ny = n
                if inp[ny%my][nx%mx] != "#":
                    if n not in cpos and n not in npos:
                        npos.add(n)
                        if i % 2 == rem:
                            tot += 1
            
        cpos = bpos
        bpos = npos

        if (i-(mx//2)) % (mx*4) == 0:
            #pvs.append(tot)
            #if len(pvs) >= 40:

            delt = tot - ptot
            acel = delt - pdelt
            dd = acel - pacel
            ddd = dd - pdd
            #print(f"iter: {i}, delta:{delt}, acel:{acel}, da:{dd}, ddd:{ddd} tot:{tot}, dp:{tot - predict}")
            ptot = tot
            pdelt = delt
            pdd = dd
            pacel = acel
            if tot - predict == 0:
                print("hit")
                while i < steps:
                    i += mx*4
                    delt += acel 
                    tot += delt 
                print(f"iter: {i}, delta:{delt}, tot:{tot}")
                return tot
            predict = tot + delt + acel
            
    return tot






if __name__ == "__main__":
    inp = get_input(2023, 21)
    test = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".splitlines()
    #if test != [""]:
        #part_one(test)
    #exit()

    #ans = part_one(inp)
    #submit(2023, 21, 1, ans)
    

    #if test != [""]:
        #part_two(test, 506)
    #exit()
    # 154126927732932
    # 639051562268397
    # 639051580070842
    # 639061037654347
    # 639051508962216
    # 639051580070842
    # 1278103017924432
    ans = part_two(inp)
   # submit(2023, 21, 2, ans)
