from advent import get_input, solution_timer, submit
from advent.helpers import *

import re

@solution_timer(2024, 3, 1)
def part_one(inp: list[str]):
    ans = 0
    for i in inp:
        x = re.findall(r"mul\((\d+),(\d+)\)", i)
        for j in x:
            x, y = map(int, j)
            ans += x * y
    return ans


@solution_timer(2024, 3, 1)
def part_two(inp: list[str]):
    inp = "".join(inp)
    ans = 0
    mul = True
    dopos = [ m.start(0) for m in re.finditer(r"do\(\)", inp)]
    dontpos = [ m.start(0) for m in re.finditer(r"don't\(\)", inp)]
    a = []
    for i in range(len(inp)):
        if i in dontpos:
            a.append(False)
            mul = False
        elif i in dopos:
            a.append(True)
            mul = True
        elif mul:
            a.append(True)
        else:
            a.append(False)

    for m in re.finditer(r"mul\((\d+),(\d+)\)", inp):
        pos = m.start(0)
        print(pos)
        x, y = map(int, m.groups())
        if a[pos]:
            ans += x * y
    return ans


if __name__ == "__main__":
    inp = get_input(2024, 3, split_char="\n")
    # ans = part_one(inp)
    # submit(2024, 3, 1, ans)
    part_two(inp)
