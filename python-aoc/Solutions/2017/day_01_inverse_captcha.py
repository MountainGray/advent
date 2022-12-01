from advent import submit, get_input
inp = get_input(2017, 1)
print(inp)
s = 0
for i in range(len(inp)):
    if inp[i] == inp[(i+(len(inp)//2))%len(inp)]:
        s += int(inp[i])
print(s)
#submit(2017, 1, 2, s)