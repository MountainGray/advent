from advent import get_input, solution_timer, submit

N = (0, -1)
S = (0, 1)
E = (1, 0)
W = (-1, 0)



pipe_dix = {
    "|":  (N, S),
    "-":  (E, W),
    "L":  (N,  E),
    "J":  (N, W),
    "7":  (S, W),
    "F":  (S, E),
    #"S":  (N, S, E, W),
}


@solution_timer(2023, 10, 1)
def part_one(inp):
    loopscores = {}
    sx, sy = 0, 0
    for idx, x in enumerate(inp):
        if "S" in x:
            sy = idx
            sx = x.index("S")
            break
    #print(sx, sy)
    
    grid = [list(x) for x in inp]
    def recur_maze(position, prev):
        x, y = position
        c = 0
        while True:
            # bound check
            c += 1
            if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
                return
            #
            pipe = grid[y][x]
            if pipe == "S":
                loopscores[position] = c
                return
            elif pipe == ".":
                return

            dirs = pipe_dix[pipe]
            ndir = dirs[0] if dirs[0] != prev else dirs[1]
            x, y = (x + ndir[0], y + ndir[1])
            if ndir == N:
                prev = S
            elif ndir == S:
                prev = N
            elif ndir == E:
                prev = W
            else:
                prev = E
        
    
    for x, y, cdir in [(0, 1, N), (1, 0, W), (-1, 0, E), (0, -1, S)]:
        recur_maze((sx + x, sy + y), cdir)

    return (max(loopscores.values()) + 1)//2



@solution_timer(2023, 10, 2)
def part_two(inp):
    loopscores = {}
    sx, sy = 0, 0
    for idx, x in enumerate(inp):
        if "S" in x:
            sy = idx
            sx = x.index("S")
    
    grid = [list(x) for x in inp]
    vlwalls = []
    def recur_maze(position, sdir):
        x, y = position
        c = 0
        lwal =[]
        prev = sdir

        while True:
            # bound check
            c += 1
            if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
                return
            lwal.append((x, y))
            #
            pipe = grid[y][x]
            if pipe == "S":
                loopscores[position] = c
                vlwalls.append(lwal)
                return
            elif pipe == ".":
                return

            dirs = pipe_dix[pipe]
            ndir = dirs[0] if dirs[0] != prev else dirs[1]
            x, y = (x + ndir[0], y + ndir[1])
            if ndir == N:
                prev = S
            elif ndir == S:
                prev = N
            elif ndir == E:
                prev = W
            else:
                prev = E

    for x, y, cdir in [(0, 1, N), (1, 0, W), (-1, 0, E), (0, -1, S)]:
        recur_maze((sx + x, sy + y), cdir)
    # unpack sub lists into vlwalls

    vlwalls = [x for y in vlwalls for x in y]
    # remove non vlwalls

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == ".":
                continue
            if (x, y) not in vlwalls:
                grid[y][x] = "."

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            print(grid[y][x], end="")
        print()

    ans = 0
    for x in range(len(grid[0])):
        nwals = 0
        nt = []
        for i in range(len(grid)):
            if grid[i][x] == "." and nwals % 2 == 1:
                ans += 1
                continue

            print(x, i)
            if grid[i][x] == "-":
                nwals += 1
            elif grid[i][x] == "F":
                nt.append("F")
            elif grid[i][x] == "7":
                nt.append("7")
            elif grid[i][x] == "L":
                pd = nt.pop()
                if pd == "7":
                    nwals += 1
            elif grid[i][x] == "J":
                pd = nt.pop()
                if pd == "F":
                    nwals += 1
    
    return ans

    

if __name__ == "__main__":

    inp = get_input(2023, 10)
    part_one(inp)
    part_two(inp)
    #submit(2023, 10, 2, ans)

