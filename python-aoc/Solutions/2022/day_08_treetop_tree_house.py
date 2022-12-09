from advent import get_input, solution_timer, get_input_grid
from itertools import product
import numpy as np

@solution_timer(2022, 8, 1)
def part_one(inp):
    grid = np.array(inp)
    dim = len(inp)
    ans = 0
    for i, j in product(range(dim), repeat=2):
        tree = grid[i][j]
        if j==0 or np.amax(grid[i,:j]) < tree: ans += 1
        elif j==dim-1 or np.amax(grid[i,j+1:]) < tree: ans +=1
        elif i==0 or np.amax(grid[:i,j]) < tree: ans += 1
        elif i==dim-1 or np.amax(grid[i+1:,j]) < tree: ans +=1

    return ans

@solution_timer(2022, 8, 2)
def part_two(inp):
    dim = len(inp)
    grid = [[int(i) for i in line] for line in inp]
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    
    ms = 0
    for i in range(dim):
        for j in range(dim):
            if i==0 or j==0 or i==dim-1 or j==dim-1:
                continue
            ss = 1
            for dx, dy in dirs:
                x = 1
                a, b = i+dx, j+dy
                while True:
                    if  a<0 or b<0 or a>=dim or b>=dim or grid[a][b] >= grid[i][j]:
                        break
                    a, b = a+dx, b+dy
                    x +=1
                ss *= x
            ms = max(ms, ss)
    return ms

if __name__ == "__main__":
    input = get_input_grid(2022, 8, int)
    part_one(input)
    part_two(input)
    