from advent import get_input, solution_timer
from sys import setrecursionlimit
setrecursionlimit(10000)

N = (0, -1)
S = (0, 1)
E = (1, 0)
W = (-1, 0)

@solution_timer(2023, 16, 1)
def part_one(inp):
    inp = [[c for c in line] for line in inp]
    energized = []

    def recur(pos, dd):
        x,y = pos
        dx, dy = dd
        if x < 0 or y  < 0 or x >= len(inp[0]) or y>= len(inp):
            return
        if (pos, dd) in energized:
            return
        energized.append((pos, dd))
        
        if inp[y][x] == ".":
            recur((x+dx, y+dy), dd)
        if inp[y][x] == "|":
            if dx != 0:
                recur((x, y+1), S)
                recur((x, y-1), N)
            else:
                recur((x+dx, y+dy), dd)
        if inp[y][x] == "-":
            if dy != 0:
                recur((x+1, y), E)
                recur((x-1, y), W)
            else:
                recur((x+dx, y+dy), dd)
        if inp[y][x] == "\\":
            if dd == N:
                recur((x-1, y), W)
            if dd == S:
                recur((x+1, y), E)
            if dd == E:
                recur((x, y+1), S)
            if dd == W:
                recur((x, y-1), N)
        if inp[y][x] == "/":
            if dd == N:
                recur((x+1, y), E)
            if dd == S:
                recur((x-1, y), W)
            if dd == E:
                recur((x, y-1), N)
            if dd == W:
                recur((x, y+1), S)

    recur((0, 0), E)

    return len(set([x[0] for x in energized]) )

            

@solution_timer(2023, 16, 2)
def part_two(inp):
    inp = [[c for c in line] for line in inp]

    energized = []

    def recur(pos, dd):
        x,y = pos
        dx, dy = dd
        rc = []
        while True:
            if x < 0 or y < 0 or x >= len(inp[0]) or y >= len(inp):
                for p in rc:
                    recur(p[0], p[1])
                return

            if ((x, y), (dx,dy)) in energized:
                for p in rc:
                    recur(p[0], p[1])
                return
            energized.append(((x,y), (dx, dy)))

            match inp[y][x]:
                case ".": 
                    x += dx
                    y += dy
                case "|":
                    if dx != 0:
                        rc.append(((x, y+1), S))
                        y -= 1
                        dx, dy = N
                    else:
                        x += dx
                        y += dy
                case "-":
                    if dy != 0:
                        rc.append(((x+1, y), E))
                        x-=1; dx, dy = W
                    else:
                        x += dx
                        y += dy
                case "\\":
                    match (dx, dy):
                        case (0, -1):
                            x -= 1
                            dx, dy = W
                        case (0, 1):
                            x += 1
                            dx, dy = E
                        case (1, 0):
                            y += 1
                            dx, dy = S
                        case (-1, 0):
                            y -= 1
                            dx, dy = N
                case "/":
                    match (dx, dy):
                        case (0, -1):
                            x += 1
                            dx, dy = E
                        case (0, 1):
                            x -= 1
                            dx, dy = W
                        case (1, 0):
                            y -= 1
                            dx, dy = N
                        case (-1, 0):
                            y += 1
                            dx, dy = S

    recur((3, 0), S)
    m = len(set([x[0] for x in energized]) )
    # go around the outside
    for x in range(len(inp[0])):
        energized = []
        recur((x, 0), S)
        tm = len(set([x[0] for x in energized]) )
        m = max(m, tm)
    
    for x in range(len(inp[0])):
        energized = []
        recur((x, len(inp)-1), N)
        tm = len(set([x[0] for x in energized]) )
        m = max(m, tm)
    
    for y in range(len(inp)):
        energized = []
        recur((0, y), E)
        tm = len(set([x[0] for x in energized]) )
        m = max(m, tm)
    
    for y in range(len(inp)):
        energized = []
        recur((len(inp[0])-1, y), W)
        tm = len(set([x[0] for x in energized]) )
        m = max(m, tm)


    return m 

if __name__ == "__main__":
    inp = get_input(2023, 16)
    inp = get_input(2023, 16, filename="test.txt")
    part_one(inp)
    part_two(inp)
