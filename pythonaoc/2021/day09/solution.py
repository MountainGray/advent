inp = open('2021/day09/input.txt').read().split('\n')
lev = [[int(x) for x in line]for line in inp]
risk = 0
height = len(lev)
width = len(lev[0])-1
floor = []
basin_map = [[0 for x in range(width+1)]for y in range(height)]
for i, line in enumerate(lev):
    for j, val in enumerate(line):
        bottom = True
        if i > 0 and lev[i-1][j] <= lev[i][j]:
                bottom = False
        if i < len(lev) - 1 and lev[i+1][j] <= lev[i][j]:
                bottom = False
        if j > 0 and lev[i][j-1] <= lev[i][j]:
                bottom = False
        if j < width and lev[i][j+1] <= lev[i][j]:
                bottom = False
        if bottom:
            risk += val + 1
            floor.append((i, j))
            basin_map[i][j] = len(floor)
print("P1:",risk)
num_basins = len(floor)
changed = True
while changed:
    changed = False
    for i, line in enumerate(lev):
        for j, val in enumerate(line):
            if basin_map[i][j] or val == 9:
                continue
            if i > 0:
                if (i-1,j) in floor:
                    basin_map[i][j] = basin_map[i-1][j]
                    floor.append((i,j))
                    changed = True
            if i < len(lev) - 1:
                if (i+1,j) in floor:
                    basin_map[i][j] = basin_map[i+1][j]
                    floor.append((i,j))
                    changed = True
            if j > 0:
                if (i,j-1) in floor:
                    basin_map[i][j] = basin_map[i][j-1]
                    floor.append((i,j))
                    changed = True
            if j < width:
                if (i,j+1) in floor:
                    basin_map[i][j] = basin_map[i][j+1]
                    floor.append((i,j))
                    changed = True

fin = [0 for _ in range(num_basins+1)]
for i in range(height):
    for j in range(width+1):
        fin[basin_map[i][j]] += 1
nums = sorted(fin[1:], reverse=True)
print("P2:",nums[0] * nums[1] * nums[2])