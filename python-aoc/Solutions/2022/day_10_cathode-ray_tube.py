from advent import get_input, print_grid, solution_timer

@solution_timer(2022, 10, 1)
def part_one(inp):
    reg = 1
    cycle =0
    ss = 0
    for i in inp:
        i = i.split()
        if i[0]=="addx":
            delt = 2
        else:
            delt = 1
        for j in range(delt):
            cycle +=1
            if (cycle - 20)%40 == 0:
                ss += reg * cycle
        if i[0]=="addx":
            reg += int(i[1])
    return ss

@solution_timer(2022, 10, 2)
def part_two(inp):
    crt = [['.' for _ in range(40)] for _ in range(6)]
    reg = 1
    cycle =0
    for i in inp:
        i = i.split()
        if i[0]=="addx":
            delt = 2
        else:
            delt = 1
        for j in range(delt):
            if -1<=(cycle%40)-reg and (cycle%40)-reg<=1:
                crt[cycle//40][cycle%40] = "#"
            cycle +=1
        if i[0]=="addx":
            reg += int(i[1])
    print_grid(crt)
    return "BGKAEREZ"

if __name__ == "__main__":
    input = get_input(2022, 10)
    part_one(input)
    part_two(input)