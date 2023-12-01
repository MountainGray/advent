from advent import get_input
inp = get_input(2016, 3)

tri = []
for i in inp:
    tri.append(list(map(int, i.split())))

impossible = 0

for x, y, z in tri:
    if x + y <= z or x + z <= y or y + z <= x:
        impossible += 1
print("P1: ", len(inp)- impossible)

impossible = 0

for i in range(0, len(tri), 3):
    for j in range(3):
        x, y, z = tri[i][j], tri[i+1][j], tri[i+2][j]
        print(x, y, z)
        if x + y <= z or x + z <= y or y + z <= x:
            impossible += 1
print(len(inp) - impossible)