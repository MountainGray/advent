from advent import get_input, solution_timer
grid = {}

@solution_timer(2022, 14, 1)
def part_one(inp):
    for i in inp:
        points = i.split(" -> ")
        for j in range(1, len(points)):
            x0, y0, x, y = map(int, [*points[j-1].split(","), *points[j].split(",")])
            for i in range(min(x0,x), max(x0,x)+1):
                for j in range(min(y0,y), max(y0,y)+1):
                    grid[(i,j)] = 0

    ymax = max(grid.keys(), key=lambda x: x[1])[1]
    sx, sy = (500, 0)
    while True:
        if (sx, sy+1) not in grid: sy += 1
        elif (sx-1, sy+1) not in grid: sx-=1; sy+=1
        elif (sx+1, sy+1) not in grid: sx+=1; sy+=1
        else: grid[(sx, sy)] = 1; sx = 500; sy = 0
        if sy > ymax: break
    return sum(grid.values())
            
@solution_timer(2022, 14, 2)
def part_two(inp):
    global grid
    grid = dict(filter(lambda x: x[1] == 0, grid.items()))
    bottom = max(grid.keys(), key=lambda x: x[1])[1] + 2
    for i in range(0,1000): grid[(i, bottom)] = 0

    sx, sy = top = (500, 0)
    while True:
        if (sx, sy+1) not in grid: sy += 1
        elif (sx-1, sy+1) not in grid: sx-=1; sy+=1
        elif (sx+1, sy+1) not in grid: sx+=1; sy+=1
        elif (sx, sy)==top: grid[top]=1;break
        else: grid[(sx, sy)] = 1; sx = 500; sy = 0
    return sum(grid.values())

if __name__ == '__main__':
    input = get_input(2022, 14)
    part_one(input)
    part_two(input)
