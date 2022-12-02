from advent import get_input, solution_timer

@solution_timer(2017, 2, 1)
def part_1(inp):
    ans = 0
    for x in inp:
        l = [int(y) for y in x.split()]
        d = max(l) - min(l)
        ans +=d
    return ans

@solution_timer(2017, 2, 2)
def part_2(inp):
    ans = 0
    for x in inp:
        l = [int(y) for y in x.split()]
        for i in range(len(l)):
            for j in range(len(l)):
                if i != j and l[i] % l[j] == 0:
                    ans += l[i] // l[j]
    return ans

if __name__ == '__main__':
    input = get_input(2017, 2)
    part_1(input)
    part_2(input)

