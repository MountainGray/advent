from advent import get_input, solution_timer
from advent.helpers import *


@solution_timer(2023, 25, 1)
def part_one(inp):
    g = nx.Graph()
    for line in inp:
        a, b = line.split(": ")
        for c in b.split(" "):
            g.add_edge(a, c)

    for x, y in minimum_edge_cut(g):
        g.remove_edge(x, y)
    return prod([len(x) for x in nx.connected_components(g)])


if __name__ == "__main__":
    inp = get_input(2023, 25)
    ans = part_one(inp)
