from advent import get_input, solution_timer
from advent.helpers import *
from math import log10, floor

import re
def getints(s):
    a = re.compile(r"(\d+)")
    return [int(x) for x in a.findall(s)]

@solution_timer(2024, 7, 1)
def part_one(inp: list[str]):
    ans = 0
    for i in inp:
        s, *ns= getints(i) 
        ps = {ns[0]}
        for i in ns[1:]:
            ps = {x + i for x in ps} | {x * i for x in ps}
        if s in ps:
            ans += s
    return ans



@solution_timer(2024, 7, 2)
def part_two(inp: list[str]):
    ans = 0
    for i in inp:
        s, *ns= getints(i) 
        ps = {ns[0]}
        for i in ns[1:]:
            ps = {x + i for x in ps} | {x * i for x in ps} | {x * 10**(floor(log10(i)) + 1) + i for x in ps}
        if s in ps:
            ans += s
    return ans

if __name__ == "__main__":
    inp = get_input(2024, 7, split_char="\n")
    part_one(inp)
    part_two(inp)
