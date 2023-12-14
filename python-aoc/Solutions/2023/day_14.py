from advent import get_input, solution_timer


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
    ly = len(inp)
    for _, y in rocks:
        ans += ly - y
    return ans


@solution_timer(2023, 14, 2)
def part_two(inp):
    dim = len(inp)
    assert dim == dim
    grid: list[list[str]] = [[x for x in line] for line in inp]

    def rotate(grid):
        for _ in range(4):
            for x in range(dim):
                bp = 0
                for y in range(dim):
                    if  grid[y][x] == "#":
                        bp = y+1
                    elif grid[y][x] == "O":
                        grid[y][x] = "."
                        grid[bp][x] = "O"
                        bp += 1
            # rotate grid
            grid = [[grid[y][x] for y in range(dim-1, -1, -1)] for x in range(dim)]
        return grid


    def score(grid):
        ans = 0
        for idy, line in enumerate(grid):
            for char in line:
                if char == "O":
                    ans += dim - idy
        return ans

    hist = []
    gi = 0
    past = 0
    for i in range(1000000000):

        grid = rotate(grid)

        hsh = "".join(["".join(line) for line in grid])

        if hsh in hist:
            gi = i
            ppoint = hist.index(hsh)
            past = len(hist) - ppoint
            print("found", i, ppoint, past)
            break

        hist.append(hsh)

        if i % 1000 == 0:
            print(i)
        
    rem = 1000000000 - gi - 1
    rem %= past

    for i in range(rem):
        grid = rotate(grid)


    return score(grid)




if __name__ == "__main__":
    inp = get_input(2023, 14)
    part_one(inp)
    part_two(inp)
