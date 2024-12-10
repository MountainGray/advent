from advent import get_input, solution_timer
from advent.helpers import *

def parse(inp) -> tuple[list[list[int]], list[tuple[int,int]]]:
    m = [[int(c) for c in l] for l in inp]
    sp = []
    for idy, l in enumerate(m):
        for idx, c in enumerate(l):
            if c == 0:
                sp.append((idx,idy))
    return (m, sp)

def recur(m, pos):
    dx, dy = pos
    if m[dy][dx] == 9:
        return [(dx,dy)]
    else:
        v = m[dy][dx] + 1
        ans = [] 
        for dx,dy in grid_ud_neigbours(pos):
            if dx >=0 and dx < len(m) and dy >=0 and dy <len(m):
                if m[dy][dx] == v:
                    ans = ans + recur(m,(dx,dy))
        return ans

@solution_timer(2024, 10, 1)
def part_one(inp: list[str]):
    m, sp = parse(inp)
    return sum([len(set(recur(m, p))) for p in sp])

@solution_timer(2024, 10, 2)
def part_two(inp: list[str]):
    m, sp = parse(inp)
    return sum([len(recur(m, p)) for p in sp])

if __name__ == "__main__":
    inp = get_input(2024, 10, split_char="\n")
    part_one(inp)
    part_two(inp)
