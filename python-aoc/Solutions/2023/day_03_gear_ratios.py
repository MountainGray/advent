from advent import get_input, solution_timer
from advent.helpers import defaultdict, grid_4_neigbours

@solution_timer(2023, 3, 1)
def part_one(inp):
    y_dim, x_dim = len(inp), len(inp[0])
    inp = defaultdict(lambda: '.', {(x,y): c for y, line in enumerate(inp) for x, c in enumerate(line)})
    ans = 0
    part_val = 0
    group = False
    valid = False
    for y in range(y_dim):
        for x in range(x_dim):
            val = inp[(x,y)]
            if val.isnumeric():
                part_val = part_val * 10 + int(val)
                group = True
                if not valid:
                    # look in nearby cells for for a symbol
                    for (i, j) in grid_4_neigbours((x,y)):
                        if inp[(i,j)] != '.' and not inp[(i,j)].isnumeric():
                            valid = True
                            break
            else: # mid line char
                if group:
                    if valid:
                        ans += part_val
                    group = False
                    valid = False
                    part_val = 0
        # end of line
        if group:
            if valid:
                ans += part_val
            group = False
            valid = False
            part_val = 0

    return ans

@solution_timer(2023, 3, 2)
def part_two(inp):
    y_dim, x_dim = len(inp), len(inp[0])
    inp = defaultdict(lambda: '.', {(x,y): c for y, line in enumerate(inp) for x, c in enumerate(line)})
    ans = 0
    gears = defaultdict(list)
    part_val = 0
    group = False
    lgear = set()

    for y in range(y_dim):
        for x in range(x_dim):
            char = inp[(x,y)]
            if char.isnumeric():
                part_val = part_val * 10 + int(char)
                group = True
                # look in nearby cells for for a symbol
                for (i, j) in grid_4_neigbours((x,y)):
                    if inp[(i,j)] == '*':
                        lgear.add((i,j))
            else:
                if group: # mid line char
                    for gear in lgear:
                        gears[gear].append(part_val)
                    part_val = 0
                    group = False
                    lgear = set()
        if group:
            for gear in lgear:
                gears[gear].append(part_val)
            part_val = 0
            group = False
            lgear = set()

    for val in gears.values():
        if len(val) == 2:
            ans += val[0] * val[1]
    return ans

if __name__ == '__main__':
    inp = get_input(2023, 3)
    part_one(inp)
    part_two(inp)
