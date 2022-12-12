from advent import get_input, solution_timer

from advent import get_input, submit 
inp = get_input(2022, 12)
#inp = '''Sabqponm
#abcryxxl
#accszExk
#acctuvwj
#abdefghi'''.splitlines()
ans = 0
grid = [list(map(ord, line)) for line in inp]
sord = ord("S")
eord = ord("E")

start_pos = (0, 0)
for y, line in enumerate(grid):
    if sord in line:
        start_pos = (line.index(sord), y)
        break
end_pos = (0, 0)
for y, line in enumerate(grid):
    if eord in line:
        end_pos = (line.index(eord), y)
        break
# increase max recursion depth
import sys
sys.setrecursionlimit(10000)

# dijkstra 

m = -1
map = [[-1 for i in range(len(grid[0]))] for _ in range(len(grid))]
def djikstra(pos, cost):
    if m != -1 and cost > m:
        return
    if cost < map[pos[1]][pos[0]] or map[pos[1]][pos[0]] == -1:
        map[pos[1]][pos[0]] = cost
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (pos[0] + x, pos[1] + y)
            if 0 <= new_pos[0] and new_pos[0] < len(grid[0]) and 0 <= new_pos[1] and new_pos[1] < len(grid) and (
                    (grid[new_pos[1]][new_pos[0]] - grid[pos[1]][pos[0]] <= 1 and grid[new_pos[1]][new_pos[0]]!=ord("E")) or ((grid[new_pos[1]][new_pos[0]] == ord("E")) and grid[pos[1]][pos[0]] == ord("z")) or ((grid[new_pos[1]][new_pos[0]] == ord("a")) and grid[pos[1]][pos[0]] == ord("S"))):
                djikstra(new_pos, cost + 1)
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == ord("a"):
            start_pos = (x, y)
            djikstra(start_pos, 0)
            ans = map[end_pos[1]][end_pos[0]]
            if m == -1 or ans < m:
                if ans != -1:
                    m = ans

print(m)

print(map)
print(ans)
#submit(2022, 12, 1, ans)

