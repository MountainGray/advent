inp = open("2020/day03/input.txt").read().split("\n")

width = len(inp[0])
# p1
x = 0
trees = 0
for row in inp:
    if row[x] == "#":
        trees += 1
    x = (x + 3) % width
print("P1:", trees)

# p2
total = 1
for angle in range(1, 8, 2):
    trees = 0
    x = 0
    for row in inp:
        if row[x] == "#":
            trees += 1
        x = (x + angle) % width
    total *= trees

x=0
trees = 0
for row in [inp[x] for x in range(0,len(inp),2)]:
    if row[x]=="#":
        trees += 1
    x = (x + 1) % width
total *= trees

print("P2", total)
