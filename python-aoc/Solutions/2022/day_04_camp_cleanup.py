from advent import get_input, solution_timer
import re

@solution_timer(2022, 4, 1)
def part_one(inp):
    ans = 0
    for i in inp:
        a1, a2, b1, b2 = map(int, re.split(",|-",i))
        if a1 <= b1 and a2 >= b2: ans += 1
        elif a1 >= b1 and a2 <= b2: ans += 1
    return ans

@solution_timer(2022, 4, 2)
def part_two(inp):
    ans = 0
    for i in inp:
        a1, a2, b1, b2 = map(int, re.split(",|-",i))
        if a1 <= b1 and a2 >= b1: ans += 1
        elif a1 >= b1 and a1 <= b2: ans += 1
    return ans


if __name__ == "__main__":
    input = get_input(2022, 4)
    part_one(input)
    part_two(input)
