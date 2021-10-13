inp = open("2015/day01/input.txt").read().split("\n")

# Part 1
floor = 0
for ch in inp[0]:
    if ch == "(":
        floor += 1

    elif ch == ")":
        floor -= 1
print("P1:", floor)
# Part 2
floor = 0
bmstp = 0
for ind, ch in enumerate(inp[0]):
    if floor == -1:
        bmstp = ind + 1
        break
    elif ch == "(":
        floor += 1
    elif ch == ")":
        floor -= 1
print("P2:", bmstp)
