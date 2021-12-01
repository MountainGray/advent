inp = [int(x) for x in open("2021/day01/input.txt").read().split("\n")]
total = 0
for x in range(1, len(inp) - 1):
    if inp[x] > inp[x - 1]:
        total += 1
print("P1:", total)
total = 0
for x in range(2, len(inp) - 1):
    if inp[x + 1] > inp[x - 2]:
        total += 1
print("P2:", total)
