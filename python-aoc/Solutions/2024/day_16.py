from advent import get_input, solution_timer
from advent.helpers import *

CMAX = 1000000000000

@solution_timer(2024, 16, 1)
def part_one(inp: list[str]):
    s = (1, len(inp) - 2)
    e = ((len(inp)-2), 1)
    d = (1, 0)

    cost = defaultdict(lambda: CMAX)

    def flr_dir(d):
        return [(d, 0), ((d[1], -d[0]), 1000), ((-d[1], d[0]), 1000)]

    def bfs_grid(s, d, e):
        q = [(s, d, 0, [s])]
        while q:
            pos, d, c, path = q.pop(0)
            if pos == e:
                    continue
            for nd, tc in flr_dir(d):
                p = (pos[0] + nd[0], pos[1] + nd[1])
                if inp[p[1]][p[0]] != "#":
                    if c + 1 + tc < cost[p]:
                        cost[p] = c + 1 + tc
                        q.append((p, nd, c + 1 + tc, path + [p]))

    bfs_grid(s, d, e)
    return cost[e]


@solution_timer(2024, 16, 2)
def part_two(inp: list[str]):
    s = (1, len(inp) - 2)
    e = ((len(inp)-2), 1)
    d = (1, 0)

    cost = defaultdict(lambda: CMAX)
    ppos = set()

    def flr_dir(d):
        return [(d, 0), ((d[1], -d[0]), 1000), ((-d[1], d[0]), 1000)]

    trgt = CMAX

    def bfs_grid(s, d, e):
        nonlocal trgt, ppos
        
        q = [(s, d, 0, [s])]
        while q:
            pos, d, c, path = q.pop(0)
            if pos == e:
                if c < trgt:
                    trgt = c
                    ppos = set(path)
                elif c == trgt:
                    for x in path:
                        ppos.add(x)
                continue
            for nd, tc in flr_dir(d):
                p = (pos[0] + nd[0], pos[1] + nd[1])
                if inp[p[1]][p[0]] != "#":
                    if c + 1 + tc < cost[p] + 2000:
                        if c + 1 + tc < cost[p]:
                            cost[p] = c + 1 + tc
                        q.append((p, nd, c + 1 + tc, path + [p]))

    bfs_grid(s, d, e)
    return len(ppos)

if __name__ == "__main__":
    inp = get_input(2024, 16, split_char="\n")
    part_one(inp)
    part_two(inp)
