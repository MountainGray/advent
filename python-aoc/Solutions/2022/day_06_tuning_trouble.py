from advent import get_input, solution_timer

@solution_timer(2022, 6, 1)
def part_one(inp):
    for i in range(4, len((inp))):
        if 4 == len(set(inp[i-4:i])): return i

@solution_timer(2022, 6, 2)
def part_two(inp):
    for i in range(14, len((inp))):
        if 14 == len(set(inp[i-14:i])): return i

if __name__ == "__main__":
    input = get_input(2022, 6)[0]
    part_one(input)
    part_two(input)