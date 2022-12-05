from advent import get_input, solution_timer

def get_stacks(inp):
    stacks = [[] for i in range(9)]
    for i in range(8):
        for j in range(9):
            stacks[j].append(inp[i][1+j*4])
    stacks = [list(filter(" ".__ne__,stack)) for stack in stacks]
    return stacks

@solution_timer(2022, 5, 1)
def part_one(inp, stacks):
    for i in inp[10:]:
        n,a,b = map(int, i.split()[1::2])
        for _ in range(n): stacks[b-1].insert(0, stacks[a-1].pop(0)) 
    return "".join([x[0] for x in stacks])


@solution_timer(2022, 5, 2)
def part_two(inp, stacks):
    for i in inp[10:]:
        n,a,b = map(int, i.split()[1::2])
        stacks[b-1] = stacks[a-1][:n]+stacks[b-1]
        stacks[a-1] = stacks[a-1][n:]
    return "".join([x[0] for x in stacks])

if __name__ == "__main__":
    input = get_input(2022, 5)
    stacks = get_stacks(input)
    part_one(input, stacks)
    part_two(input, stacks)

