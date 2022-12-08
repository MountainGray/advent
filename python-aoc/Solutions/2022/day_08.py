from advent import get_input, submit
inp = get_input(2022, 8)
grid = [[int(i) for i in line] for line in inp]
seen = set()

# check how many values increase from left to right
for i in range(len(grid)):
    m = -1
    for j in range(len(grid[i])):
        if grid[i][j] > m:
            if (i, j) in seen:
                continue
            else:
                seen.add((i, j))

            m = grid[i][j]
# check right to left
for i in range(len(grid)):
    m = -1
    for j in reversed(range(len(grid[i]))):
        if grid[i][j] > m:
            if (i, j) not in seen:
                seen.add((i, j))
            m = int(grid[i][j])
# check top to bottom
for j in range(len(grid[0])):
    m = -1
    for i in range(len(grid)):
        if grid[i][j] > m:
            if (i, j) not in seen:
                seen.add((i, j))
            m = grid[i][j]
# check bottom to top
for j in range(len(grid[0])):
    m = -1
    for i in reversed(range(len(grid))):
        if grid[i][j] > m:
            if (i, j) not in seen:
                seen.add((i, j))
            m = grid[i][j]
print(len(seen))

# find the tree that is biggest when looking in each direction
ms = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        ss = 1
        # check how many it can see to its left
        x = 0
        for k in reversed(range(j)):
            x += 1
            if grid[i][k] >= grid[i][j]:
                break
        ss *= x
        # check how many it can see to its right
        x = 0
        for k in range(j+1, len(grid[i])):
            x += 1
            if grid[i][k] >= grid[i][j]:
                break
        ss *= x
        #check how many it can see up
        x = 0
        for k in reversed(range(i)):
            x += 1
            if grid[k][j] >= grid[i][j]:
                break
        ss *= x
        # check how many it can see down
        x = 0
        # check how many it can see to its right
        for k in range(i+1, len(grid)):
            x += 1
            if grid[k][j] >= grid[i][j]:
                break
        ss *= x
        # check how many it can see to its right
        if i==0 or j==0 or i==len(grid)-1 or j==len(grid[i])-1:
            ss = 0
        ms = max(ms, ss)
print(ms)