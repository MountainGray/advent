from advent import get_input, solution_timer
from collections import defaultdict
from itertools import accumulate

fs = defaultdict(int)

@solution_timer(2022, 7, 1)
def part_one(inp):
    cd = ["/"]
    for i in inp:
        match i.split():
            case "$", "cd", "..": cd = cd[:-1]
            case "$", "cd", "/": cd = ["/"]
            case "$", "cd", x: cd = cd +[x]
            case "$", "ls": continue
            case "dir", x: continue
            case size, _:
                for dir in accumulate(cd):
                    fs[dir] += int(size)
    return sum(filter(lambda x: x <= 100_000, fs.values()))

@solution_timer(2022, 7, 2)
def part_two(inp):
    return min(filter(lambda x: x >=30_000_000 - (70_000_000-fs["/"]), fs.values()))

if __name__ == "__main__":
    input = get_input(2022, 7)
    part_one(input)
    part_two(input)