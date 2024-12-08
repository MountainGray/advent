from advent import get_input, solution_timer
from advent.helpers import *

def rdir(dir):
    x,y = dir
    return (-y,x)

@solution_timer(2024, 6, 1)
def part_one(inp: list[str]):
    a = [[x for x in i] for i in inp]
    assert(len(a[0]) == len(a))
    guard = (0,0)
    d = (0,-1)

    for (idy, y) in enumerate(a):
        for (idx, x) in enumerate(y):
            if x == "^":
                guard = (idx, idy)

    visited = set()
    while True:
        visited.add(guard)
        gx, gy = guard
        dx, dy = d
        nx, ny = gx + dx, gy + dy
        if nx < 0 or nx >= len(a) or ny < 0 or ny >= len(a):
            break
        if a[ny][nx] == "#":
            d = rdir(d)
        else:
            guard = (nx,ny)
    return len(visited)

@solution_timer(2024, 6, 1)
def part_two(inp: list[str]):
    a = [[x for x in i] for i in inp]
    guard = (0,0)
    d = (0,-1)

    for (idy, y) in enumerate(a):
        for (idx, x) in enumerate(y):
            if x == "^":
                guard = (idx, idy)

    ans = set()
    visited = set()

    while True:
        gx, gy = guard
        dx, dy = d
        nx, ny = gx + dx, gy + dy
        visited.add(guard)

        if nx < 0 or nx >= len(a) or ny < 0 or ny >= len(a):
            break

        if a[ny][nx] == "#":
            d = rdir(d)

        else:
            ng = (nx,ny)
            if ng not in visited:
                odir = d
                a[ny][nx] = "#" 
                d = rdir(d)
                vlist = set()
                found= False
                while True:
                    gx, gy = guard
                    dx, dy = d

                    nx, ny = gx + dx, gy + dy

                    if (guard, d) in vlist: # looped

                        found = True
                        break

                    else:
                        vlist.add((guard,d))

                    # no loop
                    if nx < 0 or nx >= len(a) or ny < 0 or ny >= len(a):
                        break

                    # rotate wall
                    if a[ny][nx] == "#":
                        d = rdir(d)

                    # forward
                    else:
                        guard = (nx,ny)

                # revert, stepping forward
                nx,ny = ng
                if found:
                    ans.add((nx,ny))
                a[ny][nx] = "."
                d = odir
            guard = ng

    return len(ans)

    

if __name__ == "__main__":
    inp = get_input(2024, 6, split_char="\n")
    part_one(inp)
    part_two(inp)
