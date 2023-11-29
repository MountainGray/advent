import sys
from advent import get_input

args = sys.argv[1:]

match args[0]:
    case "template":
        year, day = map(int, args[1:3])
        with open(f"python-aoc/Solutions/{year}/day_{day:02d}.py", "w") as f:
            f.write(
f"""from advent import get_input, solution_timer

@solution_timer({year}, {day}, 1)
def part_one(inp):
    pass

@solution_timer({year}, {day}, 2)
def part_two(inp):
    pass

if __name__ == "__main__":
    inp = get_input({year}, {day})
    part_one(inp)
    part_two(inp)
""")
