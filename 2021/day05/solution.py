inp = open("2021/day05/input.txt").read().split("\n")
pipes = [[int(num) for pair in line.split(" -> ") for num in pair.split(",")] for line in inp]
points = [[0 for _ in range(1000)] for _ in range(1000)]
for x1, y1, x2, y2 in pipes:
    for i in range(max(abs(x1 - x2),abs(y1-y2)) + 1):
        dx = 1 if  x1 < x2 else (-1 if x1 > x2 else 0)
        dy = 1 if  y1 < y2 else (-1 if y1 > y2 else 0)
        points[x1 + i * dx][y1 + i*dy] += 1
total = sum(map(lambda x: x > 1, [x for row in points for x in row]))
print(total)
