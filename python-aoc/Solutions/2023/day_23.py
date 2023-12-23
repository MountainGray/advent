from advent import get_input, solution_timer, submit
from advent.helpers import *
# fix recur depth
import sys
sys.setrecursionlimit(10000)


@solution_timer(2023, 23, 1)
def part_one(inp):
    start = (1, 0)
    grid = [[x for x in line] for line in inp]
    mx, my = len(grid[0]), len(grid)
    cpos = [(1, 0, 0, [])]
    mpos = defaultdict(lambda:0 )
    while len(cpos) > 0:
        x, y, d, path = cpos.pop(0)
        if d > mpos[(x,y)]:
            mpos[(x,y)] = d

        for dx,dy in iter_ud_neigbours(2):
            if 0<=x+dx<len(grid[0]) and 0<=y+dy<len(grid):
                match grid[y+dy][x+dx]:
                    case "#":
                        continue
                    case ".":
                        if [x+dx, y+dy] not in path:
                            cpos.append((x+dx, y+dy, d+1, path+[[x+dx, y+dy]]))
                    case _:
                        if [x+dx, y+dy] not in path:
                            cpos.append((x+dx, y+dy, d+1, path+[[x+dx, y+dy]]))
    return mpos[(mx-2, my-1)]

                


            




@solution_timer(2023, 23, 2)
def part_two(inp):
    start = (1, 0)
    grid = [[x for x in line] for line in inp]
    mx, my = len(grid[0]), len(grid)
    cpos = [(1, 0, 0, [])]
    mpos = defaultdict(lambda:0 )

    nodes = []

    for x,y in product(range(mx), range(my)):
        pc = 0
        if grid[y][x] == "#":
            continue
        i = 0
        for dx,dy in product([-1, 0, 1], repeat=2):
            if dx == 0 and dy == 0:
                continue
            if dx == 0 or dy == 0:
                i+=1
                if 0<=x+dx<len(grid[0]) and 0<=y+dy<len(grid):
                    match grid[y+dy][x+dx]:
                        case "#":
                            continue
                        case _:
                            pc += 1
        assert i == 4
        if pc > 2:
            nodes.append((x,y))

    nodes.append((1,0))
    nodes.append((mx-2, my-1))

    conns = defaultdict(lambda:[])
    distance = defaultdict(lambda:{})

    deltas = [(0,1), (0,-1), (1,0), (-1,0)]
    
    print("nodes")
    print(len(nodes))
    for n in nodes:
        x, y = n
        for dx,dy in deltas:
            if 0<=x+dx<len(grid[0]) and 0<=y+dy<len(grid):
                match grid[y+dy][x+dx]:
                    case "#":
                        continue
                    case _:
                        # go find next node
                        cpos = [(x, y), (x+dx,y+dy)]
                        i, j = x + dx, y + dy
                        d = 1
                        while True:
                            if (i,j) in nodes:
                                conns[n].append((i,j))
                                distance[n][(i,j)] = d
                                break
                            else:
                                for di, dj in deltas:
                                    match grid[j+dj][i+di]:
                                        case "#":
                                            continue
                                        case _:
                                            if (i+di, j+dj) not in cpos:
                                                cpos.append((i+di, j+dj))
                                                i += di
                                                j += dj
                                                d += 1
                                                #pi, pj = i, j
                                                break

                            
    def recur_mp(pos, dist, path):
        if pos == (mx-2, my-1):
            return dist
        else:
            md = 0
            for n in conns[pos]:
                if n not in path:
                    md = max(md, recur_mp(n, dist + distance[pos][n], path + [n]));
            return md
            
    print("recur")
    return recur_mp((1,0), 0, [(1,0)])


    
                



    

    return mpos[(mx-2, my-1)]

if __name__ == "__main__":
    inp = get_input(2023, 23)
    test = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#""".splitlines()
    #if test != [""]:
        #part_one(test)

    #ans = part_one(inp)
    #submit(2023, 23, 1, ans)
    

    if test != [""]:
        part_two(test)
    ans = part_two(inp)
    submit(2023, 23, 2, ans)
