from advent import get_input, solution_timer
from advent.helpers import *


@solution_timer(2024, 2, 1)
def part_one(inp: list[str]):
    ans = 0
    
    for i in inp:
        n = [int(x) for x in i.split(" ")]
        pairs = zip(n, n[1:])
        if all([abs(i - j) <= 3 for i, j in pairs]) and (
            all([i < j for i, j in zip(n, n[1:])])
            or all([i > j for i, j in zip(n, n[1:])])
        ):
            ans += 1
    return ans


@solution_timer(2024, 2, 2)
def part_two(inp):
    ans = 0
    for i in inp:
        m = i.split(" ")
        m = [int(x) for x in m]
        for d in range(len(m)):
            n = m[:d] + m[d + 1 :]
            save = True

            for i, j in zip(n, n[1:]):
                if abs(i - j) > 3:
                    save = False
                    break
            i = n[0]
            j = n[1]
            if i - j < 0:
                if not all([i < j for i, j in zip(n, n[1:])]):
                    save = False
            else:
                if not all([i > j for i, j in zip(n, n[1:])]):
                    save = False

            if save:
                ans += 1
                break
    return ans


if __name__ == "__main__":
    inp = get_input(2024, 2, split_char="\n")
    part_one(inp)
    part_two(inp)
