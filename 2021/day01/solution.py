inp = open("2021/day01/input.txt").read().split("\n")
inp = [int(x) for x in inp]
total = 0
for x in range(1,len(inp)-1):
    if inp[x]>inp[x-1]:
        total += 1

print("P1:", total)
total = 0
for x in range(2,len(inp)-1):
    if (inp[x-1]+inp[x]+inp[x+1])>(inp[x-2]+inp[x-1]+inp[x]):
        total += 1
print("P2:", total)