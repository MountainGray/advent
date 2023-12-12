from advent import get_input, solution_timer

def general(tl):
    hist = [tl]
    while True:
        ntl = []
        for i in range(len(tl) - 1):
            ntl.append(tl[i + 1] - tl[i])
        hist.append(ntl)
        tl = ntl
        if all([x == 0 for x in ntl]):
            break

    cval = 0
    tsum = 0
    for i in reversed(range(len(hist))):
        cval = hist[i][-1] + cval
        tsum += cval

    return cval


@solution_timer(2023, 9, 1)
def part_one(inp):
    ans = 0
    for line in inp:
        ans += general(list(map(int, line.split())))
    return ans


@solution_timer(2023, 9, 2)
def part_two(inp):
    ans = 0
    for line in inp:
        ans += general(list(reversed(list(map(int, line.split())))))
    return ans


if __name__ == "__main__":
    inp = get_input(2023, 9)
    part_one(inp)
    part_two(inp)
