from advent import get_input, solution_timer
from functools import lru_cache

@lru_cache(maxsize=None)
def try_seq(seq, segs) -> int:

    if len(segs) == 0:
        return 1 if all([x != "#" for x in seq]) else 0

    if len(seq) == 0:
        return 0
    
    recur_sum = 0

    cf :int = segs[0]
    for idx, val in enumerate(seq):
        if val == ".":
            continue

        if idx + cf > len(seq):
            return recur_sum

        if idx+cf < len(seq) and seq[idx+cf] == "#": # can't consume, since connected to #
            # cant continue iterating
            if val == "#":
                return recur_sum
            else:
                continue

        if all([x != "." for x in seq[idx:idx+cf]]): # note
            if val == "#":
                return recur_sum + try_seq(seq[idx+cf + 1:], segs[1:])
            else:
                recur_sum += try_seq(seq[idx+cf + 1:], segs[1:])
        else:
            if val == "#":
                return recur_sum
    
    return recur_sum


@solution_timer(2023, 12, 1)
def part_one(inp):
    ans = 0
    for line in inp:
        seq, segs = line.split()
        segs = tuple(map(int, segs.split(",")))
        ans += try_seq(seq, segs)
    return ans

@solution_timer(2023, 12, 2)
def part_two(inp):
    ans = 0
    for line in inp:
        seq, segs = line.split()
        segs = tuple(map(int, segs.split(","))) * 5
        seq = (seq + "?") * 4 + seq
        tans = try_seq(seq, segs)
        ans += tans 

    return ans

if __name__ == "__main__":
    inp = get_input(2023, 12)
    part_one(inp)
    part_two(inp)

