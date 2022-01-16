inp = open('2021/day15/input.txt').read().split('\n')
grid = [[int(x) for x in line]for line in inp]
newgrid = [[-1 for _ in range(len(inp[0])*5)] for _ in range(len(inp)*5)]
for j in range((len(inp)*5)):
    for i in range((len(inp[0])*5)):
        level = i//len(inp[0])+j//len(inp)
        newgrid[j][i] = (grid[i%len(inp[0])][j%len(inp)] + level)
for j in range((len(inp)*5)):
    for i in range((len(inp[0])*5)):
        while newgrid[j][i]>9:
            newgrid[j][i] -= 9
cost = [[-1 for _ in line] for line in newgrid]
grid = newgrid
cost[0][0]=0
changed = True
while changed:
    changed = False
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if i +1 < len(grid[0]):
                if cost[j][i+1] == -1 or cost[j][i] + grid[j][i+1] < cost[j][i+1]:
                    cost[j][i+1] = cost[j][i] + grid[j][i+1]
                    changed = True
            if i-1 >= 0:
                if cost[j][i-1] == -1 or cost[j][i] + grid[j][i-1] < cost[j][i-1]:
                    cost[j][i-1] = cost[j][i] + grid[j][i-1]
                    changed = True
            if j+1 < len(grid):
                if cost[j+1][i] == -1 or cost[j][i] + grid[j+1][i] < cost[j+1][i]:
                    cost[j+1][i] = cost[j][i] + grid[j+1][i]
                    changed = True
            if j-1 >= 0:
                if cost[j-1][i] == -1 or cost[j][i] + grid[j-1][i] < cost[j-1][i]:
                    cost[j-1][i] = cost[j][i] + grid[j-1][i]
                    changed = True
print(cost[-1][-1])
