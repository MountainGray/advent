inp = open("input/201902.txt", "r").read().split(",")
memory = list(map(int, inp))

def part1(memory):
    memory[1] = 12
    memory[2] = 2
    for i in range(0,len(inp),4):
        if memory[i] == 1:
            memory[memory[i+3]] = memory[memory[i+1]] + memory[memory[i+2]] 
        elif memory[i] == 2:
            memory[memory[i+3]] = memory[memory[i+1]] * memory[memory[i+2]]
        elif memory[i] == 99:
            break
    return memory[0]

def part2(init_memory):
    for i in range(len(init_memory)):
        for j in range(len(init_memory)):
            memory = init_memory.copy()
            memory[1] = i
            memory[2] = j
            try:
                for k in range(0,len(inp),4):
                    if memory[k] == 1:
                        memory[memory[k+3]] = memory[memory[k+1]] + memory[memory[k+2]] 
                    elif memory[k] == 2:
                        memory[memory[k+3]] = memory[memory[k+1]] * memory[memory[k+2]]
                    elif memory[k] == 99:
                        break
                if memory[0] == 19690720:
                    return 100 * i + j
            except:
                pass

print(part1(memory.copy()))
print(part2(memory.copy()))