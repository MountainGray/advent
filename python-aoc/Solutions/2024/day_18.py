from advent import get_input, solution_timer
from advent.helpers import *
from collections import deque

MDim = 71


def bfs(sx, sy, grid, cost):
    q = deque([(sx, sy, 0)])
    while q:
        x, y, c = q.popleft()
        if x < 0 or y < 0 or x >= MDim or y >= MDim or grid[y][x] == 1:
            continue
        if cost[(x, y)] <= c:
            continue
        cost[(x, y)] = c
        q.append((x + 1, y, c + 1))
        q.append((x - 1, y, c + 1))
        q.append((x, y + 1, c + 1))
        q.append((x, y - 1, c + 1))


@solution_timer(2024, 18, 1)
def part_one(inp):
    grid = [[0 for i in range(MDim)] for j in range(MDim)]
    for i in inp[:1024]:
        x, y = nums(i)
        grid[y][x] = 1

    cost = defaultdict(lambda: float("inf"))
    bfs(0, 0, grid, cost)
    return cost[(MDim - 1, MDim - 1)]


@solution_timer(2024, 18, 2)
def part_two(inp):
    grid = [[0 for i in range(MDim)] for j in range(MDim)]
    for i in inp[:1024]:
        x, y = nums(i)
        grid[y][x] = 1

    for i in inp[1024:]:
        x, y = nums(i)
        grid[y][x] = 1
        cost = defaultdict(lambda: float("inf"))
        bfs(0, 0, grid, cost)
        if cost[(MDim - 1, MDim - 1)] == float("inf"):
            return (x, y)


if __name__ == "__main__":
    inp = get_input(2024, 18)
    part_one(inp)
    part_two(inp)
