inp = open('2015/day06/input.txt').read().split('\n')[:-1]

commands= []
print(inp)
for x in inp:
    a =[]
    print("test")
    if "turn on" in x:
        a.append(0)
    elif "turn off" in x:
        a.append(1)
    else:
        print("test")
        a.append(2)
    b = x.split(" ")
    b = b[-3].split(",")+b[-1].split(",")
    a = a + [int(b[0]),int(b[1]), int(b[2]), int(b[3])]
    commands.append(a)

grid = [[0 for x in range(1000)] for y in range(1000)]
print(commands)
for x in commands:
    if x[0] == 0:
        for i in range(x[1], x[3]+1):
            for j in range(x[2], x[4]+1):
                grid[i][j] += 1
    elif x[0] == 1:
        for i in range(x[1], x[3]+1):
            for j in range(x[2], x[4]+1):
                grid[i][j] -= 1 if grid[i][j] > 0 else 0
    elif x[0] == 2:
        for i in range(x[1], x[3]+1):
            for j in range(x[2], x[4]+1):
                grid[i][j] += 2 

lights = 0
for x in grid:
    for y in x:
        lights += y

print(lights)
        
