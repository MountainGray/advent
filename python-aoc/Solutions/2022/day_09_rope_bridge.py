from advent import get_input, solution_timer
inp = get_input(2022, 9)

dirs = {"D": [0, -1], "U": [0, 1], "L": [-1, 0], "R": [1, 0]}

def solve(inp, knots):
    visited = set()
    points = [[0, 0] for i in range(knots+1)]
    for i in inp:
        i = i.split()
        d, dist = i[0], int(i[1])
        for i in range(dist):
            points[0][1] += dirs[d][1]
            points[0][0] += dirs[d][0]
            # drag tail
            for j in range(1, len(points)):
                xh, yh = points[j-1]
                xt, yt = points[j]
                if max([abs(xt-xh), abs(yt-yh)]) >1:
                    if xt>xh:
                        points[j][0] -= 1
                    elif xt<xh:
                        points[j][0] += 1
                    if yt>yh:
                        points[j][1] -= 1
                    elif yt<yh:
                        points[j][1] += 1
                if j == len(points)-1:
                    visited.add((points[j][0], points[j][1]))
    return len(visited)

@solution_timer(2022, 9, 1)
def part_one(inp):
    return solve(inp, 1)

@solution_timer(2022, 9, 2)
def part_two(inp):
    return solve(inp, 9)
        
if __name__ == "__main__":
    input = get_input(2022, 9)
    part_one(input)
    part_two(input)

#submit(2022, 9, 1, ans)
#submit(2022, 9, 2, ans)