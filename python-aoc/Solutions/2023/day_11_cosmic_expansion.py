from advent import get_input, solution_timer
from itertools import combinations


@solution_timer(2023, 11, 1)
def part_one(inp):
    return solve_generic(inp, 2)

@solution_timer(2023, 11, 2)
def part_two(inp):
    return solve_generic(inp, 1000000)

def solve_generic(inp, expansion_size: int):
    drow= []
    for idx, each in enumerate(inp):
        if all([x == "." for x in each]):
            # double the row
            drow.append(idx)

    dcol = []
    for idx in range(len(inp[0])):
        if all([x[idx] == "." for x in inp]):
            # double the column
            dcol.append(idx)
    
    points = []
    for idy, row in enumerate(inp):
        for idx, col in enumerate(row):
            if col == "#":
                points.append((idx, idy))
    
    computed = {}

    for p1, p2 in combinations(points, 2):
        x1, y1 = p1
        x2, y2 = p2
        distance = abs(x1 - x2) + abs(y1 - y2)
        change = expansion_size - 1
        for row_idx in range(min(y1, y2), max(y1, y2)):
            if row_idx in drow:
                distance += change
        for col_idx in range(min(x1, x2), max(x1, x2)):
            if col_idx in dcol:
                distance += change 

        computed[(p1, p2)] = distance
    return sum(computed.values())

if __name__ == "__main__":
    inp = get_input(2023, 11)
    part_one(inp)
    part_two(inp)

