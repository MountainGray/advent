from advent import get_input, solution_timer, submit
from advent.helpers import * # noqa F403
import numpy as np


@solution_timer(2023, 18, 1)
def part_one(inp):
    direx = []
    for line in inp:
        d, n, c = line.split()
        n = int(n)
        direx.append((d, n, c))
    max_x, max_y = 0, 0
    min_x, min_y = 0, 0
    x, y = 0, 0
    points = [(0,0)]
    for d, n, c in direx:
        match d:
            case "R":
                x += n
            case "L":
                x -= n
            case "U":
                y -= n
            case "D":
                y += n
        points.append((x, y))

        max_x = max(max_x, x)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        min_y = min(min_y, y)

    
    g = [["." for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for p1, p2 in zip(points, points[1:]):
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                g[y - min_y][x1 - min_x] = "#"
        else:
            for x in range(min(x1, x2), max(x1, x2)+1):
                g[y1 - min_y][x - min_x] = "#"
    
    for x,y in grid_neigbours((0-min_x, 0-min_y)):
        print(x,y)
        fail = False
        f = [[x for x in line] for line in g] # copy
        propogate = set(grid_neigbours((x,y)))
        marked = set()
        while len(propogate) > 0:
            x1, y1 = propogate.pop()
            if x1 < 0 or y1 < 0 or x1 >= len(f[0]) or y1 >= len(f):
                print("out of bounds")
                fail = True
                break
            marked.add((x1, y1))
            if f[y1][x1] == "#":
                continue
            else:
                neigbours = set(grid_neigbours((x1, y1)))
                neigbours -= marked
                propogate |= neigbours
        if fail:
            continue

        return len(marked) 

        
    
dirmap = {
    0: "R",
    1: "D",
    2: "L",
    3: "U"
}


@solution_timer(2023, 18, 2)
def part_two(inp):
    direx = []
    for line in inp:
        d, n, c = line.split()
        #n = int(n)
        #direx.append((d, n, c))
        c= c[2:-1]
        n = int(c[:-1], 16)
        d = dirmap[int(c[-1])]
        direx.append((d, n, c))
    max_x, max_y = 0, 0
    min_x, min_y = 0, 0
    x, y = 0, 0
    points = [(0,0)]
    for d, n, _ in direx:
        match d:
            case "R":
                x += n
            case "L":
                x -= n
            case "U":
                y -= n
            case "D":
                y += n
        points.append((x, y))

        max_x = max(max_x, x)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        min_y = min(min_y, y)

    points.reverse()

    area = 0
    j = len(points) - 1

    for i in range(len(points)):
        xi, yi = points[i]
        xj, yj = points[j]
        area += (xi + xj) * (yj - yi)
        j = i
    
    peremiter = 0
    for p1, p2 in zip(points, points[1:]):
        x1, y1 = p1
        x2, y2 = p2
        peremiter += abs(x1 - x2) + abs(y1 - y2)

    return (area // 2) + (peremiter // 2) + 1


if __name__ == "__main__":
    inp = get_input(2023, 18)
    part_one(inp)
    part_two(inp)
