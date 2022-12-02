from advent import get_input, solution_timer

@solution_timer(2017, 1, 1)
def part_1(inp):
    s = 0
    for i in range(len(inp)):
        if inp[i] == inp[(i+1)%len(inp)]:
            s += int(inp[i])
    return s

@solution_timer(2017, 1, 2)
def part_2(inp):
    s = 0
    for i in range(len(inp)):
        if inp[i] == inp[(i+(len(inp)//2))%len(inp)]:
            s += int(inp[i])
    return s


if __name__ == '__main__':
    input = get_input(2017, 1)[0]
    part_1(input)
    part_2(input)