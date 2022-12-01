from advent import get_input, solution_timer

@solution_timer(2022, 1, 1)
def part_one(inp):
    elves = list(map(sum, [map(int, x.split("\n")) for x in inp]))
    return max(elves)

@solution_timer(2022, 1, 2)
def part_two(inp):
    elves = list(map(sum, [map(int, x.split("\n")) for x in inp]))
    return sum(sorted(elves)[-3:])

if __name__=="__main__":
    inp = get_input(2022, 1, split_char="\n\n")
    part_one(inp)
    part_two(inp)