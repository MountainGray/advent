from advent import get_input, solution_timer, submit



@solution_timer(2023, 6, 1)
def part_one(inp):
    ans = 1
    races = []
    times = map(int, inp[0].split()[1:])
    dists = map(int, inp[1].split()[1:])
    races = zip(times,dists)
    for time, mdist in races:
        tsum = 0
        for i in range(time):
            if i * (time - i) > mdist:
                tsum += 1
        print(tsum)
        ans *= tsum
    return ans


@solution_timer(2023, 6, 2)
def part_two(inp):
    ans = 0
    time = int("".join(inp[0].split()[1:]))
    mdist = int("".join(inp[1].split()[1:]))
    for i in range(time):
        if i * (time - i) > mdist:
            ans += 1
    return ans


if __name__ == "__main__":
    inp = get_input(2023, 6)
    part_one(inp)
    part_two(inp)

