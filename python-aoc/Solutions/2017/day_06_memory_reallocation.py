from advent import get_input, solution_timer

@solution_timer(2017, 6, 1)
def part_one(inp):
    ans = 0
    ca = {}
    b = list(map(int, inp[0].split()))
    while True:
        if tuple(b) in ca:
            break
        else:
            ca[tuple(b)] = ans
            ans += 1
            m = max(b)
            i = b.index(m)
            b[i] = 0
            for j in range(m):
                b[(i+j+1)%len(b)] += 1
    return ans

@solution_timer(2017, 6, 2)
def part_two(inp, ans):
    ans = 0
    ca = {}
    b = list(map(int, inp[0].split()))
    while True:
        if tuple(b) in ca:
            break
        else:
            ca[tuple(b)] = ans
            ans += 1
            m = max(b)
            i = b.index(m)
            b[i] = 0
            for j in range(m):
                b[(i+j+1)%len(b)] += 1
    return ans - ca[tuple(b)]
    
if __name__ == "__main__":
    input = get_input(2017, 6)
    a = part_one(input)
    part_two(input, a)

