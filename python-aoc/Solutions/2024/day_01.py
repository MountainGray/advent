from advent import get_input, solution_timer
from advent.helpers import *

@solution_timer(2024, 1, 1)
def part_one(inp):
    ans = 0
    a,b = [], []
    for l in inp:
        x,y= l.split("   ")
        a.append(int(x))
        b.append(int(y))

    a = sorted(a)
    b = sorted(b)
    return sum([abs(x-y) for x,y in zip(a,b)])



@solution_timer(2024, 1, 2)
def part_two(inp):
    a,b = [], []
    for l in inp:
        x,y= l.split("   ")
        a.append(int(x))
        b.append(int(y))
    return sum([x *b.count(x) for x in a])

if __name__=="__main__":
    inp = get_input(2024, 1, split_char="\n")
    part_one(inp)
    part_two(inp)
