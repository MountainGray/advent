from advent import get_input, solution_timer
from advent.helpers import *

@solution_timer(2024, 8, 1)
def part_one(inp: list[str]):
    d = {}
    grid=  [[c for c in ln] for ln in inp]
    for idy, ln in enumerate(grid):
        for idx, c in enumerate(ln):
            if c != ".":
                if c not in d:
                    d[c] = []
                d[c].append((idx, idy))
    ans = set()
    for k, v in d.items():
        for (ax,ay),(bx,by) in combinations(v, 2):
            dx = ax - bx
            dy = ay - by
            adx = ax + dx
            ady = ay + dy
            if adx >= 0 and ady >= 0 and adx < len(grid[0]) and ady < len(grid):
                ans.add((adx, ady))

            dx = bx - ax
            dy = by - ay
            adx = bx + dx
            ady = by + dy
            if adx >= 0 and ady >= 0 and adx < len(grid[0]) and ady < len(grid):
                ans.add((adx, ady))
    return len(ans)



@solution_timer(2024, 8, 2)
def part_two(inp: list[str]):
    d = {}
    grid=  [[c for c in ln] for ln in inp]
    for idy, ln in enumerate(grid):
        for idx, c in enumerate(ln):
            if c != ".":
                if c not in d:
                    d[c] = []
                d[c].append((idx, idy))

    ans = set()
    for k, v in d.items():
        ans.update(v)
        for (ax,ay),(bx,by) in combinations(v, 2):
            dx = ax - bx
            dy = ay - by
            adx = ax + dx
            ady = ay + dy
            while True:
                if adx >= 0 and ady >= 0 and adx < len(grid[0]) and ady < len(grid):
                    ans.add((adx, ady))
                else:
                    break
                adx +=dx
                ady +=dy

            dx = bx - ax
            dy = by - ay
            adx = bx + dx
            ady = by + dy
            while True:
                if adx >= 0 and ady >= 0 and adx < len(grid[0]) and ady < len(grid):
                    ans.add((adx, ady))
                else:
                    break
                adx +=dx
                ady +=dy
    return len(ans)


if __name__ == "__main__":

    inp = get_input(2024, 8, split_char="\n")
    part_one(inp)
    part_two(inp)
