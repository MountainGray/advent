from advent import get_input, solution_timer, submit


@solution_timer(2023, 5, 1)
def part_one(inp):
    pass


@solution_timer(2023, 5, 2)
def part_two(inp):
    pass

if __name__ == "__main__":
    test = get_input(2023, 5, filename="test.txt")
    print("Test:")
    part_one(test)
    part_two(test)

    print("inp:")
    inp = get_input(2023, 5)
    ans = part_one(inp)
    submit(2023, 5, 1, ans)
    ans = part_two(inp)
    #submit(2023, 5, 2, ans)

