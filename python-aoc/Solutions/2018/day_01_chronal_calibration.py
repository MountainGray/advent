from advent import get_input, solution_timer

@solution_timer(2018, 1, 1)
def part_one(inp):
    return sum(int(i) for i in inp)

@solution_timer(2018, 1, 2)
def part_two(inp):
    vals = {}
    ans = 0
    while True:
        for i in inp:
            ans += int(i)
            if ans in vals.keys():
                return ans
            else:
                vals[ans]=1
            
if __name__ == "__main__":
    input = get_input(2018, 1)
    part_one(input)
    part_two(input)