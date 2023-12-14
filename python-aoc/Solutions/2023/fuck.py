from advent import get_input, solution_timer, submit
from functools import cache


@solution_timer(2023, 14, 1)
def part_one(inp):
    rocks = []
    walls = []

    for idy, line in enumerate(inp):
        for idx, char in enumerate(line):
            match char:
                case "O":
                    rocks.append((idx, idy))
                case ".":
                    continue
                case "#":
                    walls.append((idx, idy))
    

    #tilt forward

    while True:
        updated = False

        for i in range(len(rocks)):
            idx, idy = rocks[i]
            if idy > 0:
                if (idx, idy - 1) in walls:
                    continue
                elif (idx, idy - 1) in rocks:
                    continue
                else:
                    rocks[i] = (idx, idy - 1)
                    updated = True
        if not updated:
            break

    ans = 0
    plen = len(inp)
    for x, y in rocks:
        ans += plen - y
    return ans




@solution_timer(2023, 14, 2)
def part_two(inp):
    lx, ly = len(inp[0]), len(inp)
    mrocks = []
    mwalls = []
    i = 0
    for idy, line in enumerate(inp):
        for idx, char in enumerate(line):
            match char:
                case "O":
                    mrocks.append((idx, idy))
                    i += 1
                case ".":
                    continue
                case "#":
                    mwalls.append((idx, idy))
    
    #def print_grid(inp, rocks, walls):
        #for y in range(len(inp)):
            #for x in range(len(inp[0])):
                #if (x, y) in rocks:
                    #print("O", end="")
                #elif (x, y) in walls:
                    #print("#", end="")
                #else:
                    #print(".", end="")
            #print()

    @cache
    def rotate(rocks, walls):

        # tilt north
        rocks = list(rocks)
        walls = list(walls)

        #rcopy = set([x for x in rocks])
        def tilt(rocks, walls, dr):
            while True:
                new = False
                nrocks = []
                dx, dy = dr
                for i in range(len(rocks)):
                    rx, ry = rocks[i]
                    npos = None
                    if 0 <= rx + dx < len(inp[0]) and 0 <= ry + dy < len(inp):
                            if (rx + dx, ry + dy) in walls:
                                continue
                            elif (rx + dx, ry + dy) in nrocks:
                                continue
                            else:
                                npos = (rx + dx, ry + dy)
                    if npos is not None:
                        new = True
                        nrocks.append(npos)
                    
                rocks = nrocks
                if not new:
                    break
            return nrocks

        for dr in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            rocks = tilt(rocks, walls, dr)

        return tuple(rocks), tuple(walls)

    hist = []
    gi = 0
    past = 0
    #for i in range(1000000000):
    for i in range(1000000000):
    #for i in range(3):
        gi = i

        mrocks, mwalls = rotate(tuple(mrocks), tuple(mwalls))

        if hash(mrocks) in hist:
            past = len(hist) - hist.index(hash(mrocks))
            break
        hist.append(hash(mrocks))
        #print_grid(inp, mrocks, mwalls)
        #print()

        if i % 1000 == 0:
            print(i)
        
    rem = 1000000000 - gi
    rem %= past - 1

    print(gi , past,  rem)
    for i in range(rem):
        mrocks, mwalls = rotate(tuple(mrocks), tuple(mwalls))


    ans = 0
    plen = len(inp)
    for x, y in mrocks:
        ans += plen - y
    return ans



if __name__ == "__main__":
    inp = get_input(2023, 14)
    test = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".splitlines()
    #if test != [""]:
        #part_one(test)

    #ans = part_one(inp)
    

    if test != [""]:
        part_two(test)
    exit()
    ans = part_two(inp)
    submit(2023, 14, 2, ans)
