from advent import get_input, solution_timer

def tilt(grid):
    dim = len(grid)
    for x in range(dim):
        bp = 0
        for y in range(dim):
            if grid[y][x] == "#":
                bp = y + 1
            elif grid[y][x] == "O":
                grid[y][x] = "."
                grid[bp][x] = "O"
                bp += 1

def rotate(grid):
    for _ in range(4):
        tilt(grid)
        grid = list(map(list,zip(*grid[::-1])))
    return grid

def score(grid):
    dim, ans = len(grid), 0
    for idy, line in enumerate(grid):
        for char in line:
            if char == "O":
                ans += dim - idy
    return ans


@solution_timer(2023, 14, 1)
def part_one(inp):
    grid = [[x for x in line] for line in inp]
    tilt(grid)
    return score(grid)


@solution_timer(2023, 14, 2)
def part_two(inp):
    grid: list[list[str]] = [[x for x in line] for line in inp]

    hist = []
    past = 0
    
    i = 0
    while i < 1000000000:
        i += 1

        grid = rotate(grid)
        hsh = "".join(["".join(line) for line in grid])

        if hsh in hist:
            past = len(hist) - hist.index(hsh) 
            break

        hist.append(hsh)

    # remaining iterations
    rem = (1000000000 - i) % past
    for i in range(rem):
        grid = rotate(grid)

    return score(grid)

if __name__ == "__main__":
    inp = get_input(2023, 14)
    part_one(inp)
    part_two(inp)
