inp = open("2015/day02/input.txt").read().split("\n")

dims = []
for line in inp:
    dims.append(sorted([int(x) for x in line.split("x")]))

# Part 1
paper= 0
for x,y,z in dims:
    paper += 2*x*y + 2*y*z + 2*x*z + min(x*y, y*z, x*z)

print("Part 1:", paper)

# Part 2
ribbon = 0
for x,y,z in dims:
    ribbon += 2*x + 2*y + x*y*z

print("Part 2:", ribbon)

