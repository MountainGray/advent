from advent import get_input
inp = get_input(2022, 18)
ans = 0
points = set()
for i in inp:
    x,y,z = map(int, i.split(','))
    sa = 6
    for dx in [-1,0,1]:
        if (x+dx,y,z) in points: sa -= 2
    for dy in [-1,0,1]:
        if (x,y+dy,z) in points: sa -= 2
    for dz in [-1,0,1]:
        if (x,y,z+dz) in points: sa -= 2
    points.add((x,y,z))
    ans +=sa
print(ans)
ans = 0

xmin = min(x for x,y,z in points)
xmax = max(x for x,y,z in points)
ymin = min(y for x,y,z in points)
ymax = max(y for x,y,z in points)
zmin = min(z for x,y,z in points)
zmax = max(z for x,y,z in points)

steamed = set()
def find_outside(pos):
    global ans
    if pos in steamed:
        return
    steamed.add(pos)
    x,y,z = pos
    if x == xmin-2 or x == xmax+2 or y == ymin-2 or y == ymax+2 or z == zmin-2 or z == zmax+2:
        return
    for dx in [-1,1]:
        if (x+dx,y,z) in points: ans +=1
        else: find_outside((x+dx,y,z))
    for dy in [-1,1]:
        if (x,y+dy,z) in points: ans +=1
        else: find_outside((x,y+dy,z))
    for dz in [-1,1]:
        if (x,y,z+dz) in points: ans +=1
        else: find_outside((x,y,z+dz))

find_outside((0,0,0))
print(ans)

import sys
sys.setrecursionlimit(100000)

