from advent import get_input, solution_timer

def priority(a):
    return ord(a) - 64 +26 if a.isupper() else ord(a) - 96

@solution_timer(2022, 3, 1)
def part_one(inp):
    ans = 0
    for i in inp:
        a = i[:len(i)//2]
        b = i[len(i)//2:]
        for j in a:
            if j in b:
                ans += priority(j)
                break
    return ans

@solution_timer(2022, 3, 2)
def part_two(inp):
    ans = 0
    for i in range(0,len(inp),3):
        a = inp[i]
        b = inp[(i+1)]
        c = inp[(i+2)]
        for j in a:
            if j in b and j in c:
                ans += priority(j)
                break
    return ans
            
if __name__ == "__main__":
    input = get_input(2022, 3)
    part_one(input)
    part_two(input)