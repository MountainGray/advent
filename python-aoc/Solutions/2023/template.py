year = 2023
day = 17
tp = f'''
from advent import get_input, solution_timer, submit


@solution_timer({year}, {day}, 1)
def part_one(inp):
    pass


@solution_timer({year}, {day}, 2)
def part_two(inp):
    pass

if __name__ == "__main__":
    inp = get_input({year}, {day})
    test = """""".splitlines()
    if test != [""]:
        part_one(test)

    ans = part_one(inp)
    submit({year}, {day}, 1, ans)
    
    exit()

    if test != [""]:
        part_two(test)
    ans = part_two(inp)
    submit({year}, {day}, 2, ans)
'''

path = f"python-aoc/Solutions/{year}/day_{day}.py"
with open(path, "w") as f:
    f.write(tp)
