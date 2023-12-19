from advent import get_input, solution_timer, submit
from advent.helpers import *


@solution_timer(2023, 19, 1)
def part_one(inp):
    pass


@solution_timer(2023, 19, 2)
def part_two(inp):
    pass

if __name__ == "__main__":
    inp = get_input(2023, 19)
    test = """""".splitlines()
    if test != [""]:
        part_one(test)

    ans = part_one(inp)
    submit(2023, 19, 1, ans)
    
    exit()

    if test != [""]:
        part_two(test)
    ans = part_two(inp)
    submit(2023, 19, 2, ans)
