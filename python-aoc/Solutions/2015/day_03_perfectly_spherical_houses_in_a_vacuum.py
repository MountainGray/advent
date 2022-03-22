inp = open("2015/day03/input.txt").read().split("\n")


houses = {}
pos = (0, 0)
houses[pos] = 1
# Part 1
for dr in inp[0]:
    if dr == "^":
        pos = (pos[0], pos[1] + 1)
    elif dr == "v":
        pos = (pos[0], pos[1] - 1)
    elif dr == ">":
        pos = (pos[0] + 1, pos[1])
    elif dr == "<":
        pos = (pos[0] - 1, pos[1])
    houses[pos] = houses.get(pos, 0) + 1

print("P1:", len(houses))

# Part 2
santa = (0, 0)
robo = (0, 0)
houses = {}
houses[santa] = 1
for i, dr in enumerate(inp[0]):
    if i % 2 == 0:
        if dr == "^":
            santa = (santa[0], santa[1] + 1)
        elif dr == "v":
            santa = (santa[0], santa[1] - 1)
        elif dr == ">":
            santa = (santa[0] + 1, santa[1])
        elif dr == "<":
            santa = (santa[0] - 1, santa[1])
        houses[santa] = houses.get(santa, 0) + 1
    else:
        if dr == "^":
            robo = (robo[0], robo[1] + 1)
        elif dr == "v":
            robo = (robo[0], robo[1] - 1)
        elif dr == ">":
            robo = (robo[0] + 1, robo[1])
        elif dr == "<":
            robo = (robo[0] - 1, robo[1])
        houses[robo] = houses.get(robo, 0) + 1

print("P2:", len(houses))









