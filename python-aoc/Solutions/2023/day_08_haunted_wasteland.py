from advent import get_input, solution_timer, submit
from math import lcm

@solution_timer(2023, 8, 1)
def part_one(inp):
    start, end = "AAA", "ZZZ"
    seq, _, *nodes = inp
    rn = {}

    for line in nodes:
        k, _, left, right = line.split()
        left = left[1:-1]
        right = right[:-1]
        rn[k]= (left, right)

    curr = start
    i = 0
    s = 0
    while curr != end:
        s += 1
        if i >= len(seq):
            i = 0
        if seq[i] == "L":
            curr = rn[curr][0]
        else:
            curr = rn[curr][1]
        i += 1

    return s


@solution_timer(2023, 8, 2)
def part_two(inp):
    seq, _, *nodes = inp
    rn = {}

    for line in nodes:
        k, _, left, right = line.split()
        left, right= left[1:-1], right[:-1]
        rn[k]= (left, right)

    start_nodes = [x for x in rn.keys() if x[2] == "A"]
    gds = {}
    for start in start_nodes:
        curr = start
        i = 0
        s = 0
        while curr[2] != "Z":
            s += 1
            if i >= len(seq):
                i = 0
            if seq[i] == "L":
                curr = rn[curr][0]
            else:
                curr = rn[curr][1]
            i += 1
        gds[start] = s

    # return lcm of all gds
    return lcm(*gds.values())


if __name__ == "__main__":
    inp = get_input(2023, 8)
    part_one(inp)
    part_two(inp)

