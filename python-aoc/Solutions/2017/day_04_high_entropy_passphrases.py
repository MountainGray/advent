from advent import get_input, solution_timer

@solution_timer(2017, 4, 1)
def part_one(inp):
    ans = 0
    for i in inp:
        a = i.split()
        b = set(a)
        if len(a) == len(b):
            ans += 1
    return ans

@solution_timer(2017, 4, 2)
def part_two(inp):
    ans = 0
    for i in inp:
        a = i.split()
        b = set(a)
        if len(a) == len(b):
            c = ["".join(sorted(j)) for j in a]
            d = set(c)
            if len(c) == len(d):
                ans += 1
    return ans



if __name__ == "__main__":
    input = get_input(2017, 4)
    part_one(input)
    part_two(input)
