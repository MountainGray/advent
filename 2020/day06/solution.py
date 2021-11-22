groups = [x.splitlines() for x in open("2020/day06/input.txt").read().split("\n\n")]

# p1
total = 0
for group in groups:
    vals = set(group[0])
    for member in group:
        vals = vals | set(member)
    total += len(vals)
print("P1:", total)
# p2
total = 0
for group in groups:
    vals = set(group[0])
    for member in group:
        vals = vals & set(member)
    total += len(vals)
print("P2:", total)
