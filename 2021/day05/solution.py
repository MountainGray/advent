inp = open("2021/day05/input.txt").read().split("\n")
pipes = [[pair for pair in line.split(" -> ")] for line in inp]
points = {}
for pipe in pipes:
    x1, y1 = map(int ,pipe[0].split(","))
    x2, y2 = map(int, pipe[1].split(","))
    if x1 == x2:
        if y1 < y2:
            for i in range(y1, y2+1):
                if (x1, i) not in points:
                    points[(x1, i)] = 0
                points[(x1, i)] += 1
        else:
            for i in range(y2, y1+1):
                if (x1, i) not in points:
                    points[(x1, i)] = 0
                points[(x1, i)] += 1
    elif y1 == y2:
        if x1 < x2:
            for i in range(x1, x2+1):
                if (i, y1) not in points:
                    points[(i, y1)] = 0
                points[(i, y1)] += 1
        else:
            for i in range(x2, x1+1):
                if (i, y1) not in points:
                    points[(i, y1)] = 0
                points[(i, y1)] += 1
    else:
        if x1 < x2 and y1 < y2:
            for i in range(x2-x1 + 1):
                if (x1+i, y1+i) not in points:
                    points[(x1+i, y1+i)] = 0
                points[(x1+i, y1+i)] += 1
        if x1 > x2 and y1 < y2:
            for i in range(x1-x2+1):
                if (x1-i, y1+i) not in points:
                    points[(x1-i, y1+i)] = 0
                points[(x1-i, y1+i)] += 1
        if x1 < x2 and y1 > y2:
            for i in range(y1-y2+1):
                if (x1+i, y1-i) not in points:
                    points[(x1+i, y1-i)] = 0
                points[(x1+i, y1-i)] += 1
        if x1 > x2 and y1 > y2:
            for i in range(y1-y2+1):
                if (x1-i, y1-i) not in points:
                    points[(x1-i, y1-i)] = 0
                points[(x1-i, y1-i)] += 1

total = 0
for x in points.values():
    if x >= 2:
        total += 1

print(total)
