from advent import get_input, solution_timer
from sympy import *

@solution_timer(2023, 6, 1)
def part_one(inp):
    times = map(int, inp[0].split()[1:])
    dists = map(int, inp[1].split()[1:])
    races = zip(times,dists)
    ans = 1
    for time, mdist in races:
        tsum = 0
        for i in range(time):
            if i * (time - i) > mdist:
                tsum += 1
        ans *= tsum
    return ans


@solution_timer(2023, 6, 2)
def part_two(inp):
    """ Symbolic solving the range is 100x faster than an iterative approach """
    time = int("".join(inp[0].split()[1:]))
    mdist = int("".join(inp[1].split()[1:]))
    x = Symbol("x")
    sols = solveset(Eq(x * (time - x) - mdist, 0), x)
    f, l = map(int, sols)
    return (l-f)

if __name__ == "__main__":
    inp = get_input(2023, 6)
    part_one(inp)
    part_two(inp)

