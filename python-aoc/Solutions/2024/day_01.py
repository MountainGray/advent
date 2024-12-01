from advent import get_input, solution_timer
from advent.helpers import *

@solution_timer(2024, 1, 1)
def part_one(inp):
    elves = list(map(sum, [map(int, x.split("\n")) for x in inp]))
    return max(elves)

@solution_timer(2024, 1, 2)
def part_two(inp):
    pass

if __name__=="__main__":
    inp = get_input(2024, 1, split_char="\n")
    print(inp)
    part_one(inp)
    # part_two(inp)
