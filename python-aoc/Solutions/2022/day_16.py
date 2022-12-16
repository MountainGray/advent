from advent import get_input

inp = get_input(2022, 16)
valves = {}
paths = {}

for line in inp:
    i = line.split(" ")
    valve = i[1]
    rate = int(i[4][5:-1])
    valves[valve] = rate
    tunnels = i[9:]
    tunnels = [i[:-1] for i in tunnels[:-1]]+[tunnels[-1]]
    tunnels = set(tunnels)
    paths[valve] = tunnels

ltree = {}
def findpaths(start:str, position, dist:int = 1):
    for path in paths[position]:
        if (start, path) not in ltree:
            ltree[(start, path)] = dist
            findpaths(start, path, dist+1)
        elif ltree[(start, path)] > dist:
            ltree[(start, path)] = dist
            findpaths(start, path, dist+1)


for i in valves.keys():
    findpaths(i, i)

matter = list(filter(lambda x: x[1] > 0, valves.items()))
vlist = [x[0] for x in matter]
vset= set((x[0] for x in matter))
    
start = "AA"
t: int = 30
ans :int= -1
def s_tree(position, time, on: set, flow):
    global ans
    if flow > ans:
        ans = flow
    for j in vset.difference(on):
        if ltree[(position, j)] < time-1:
            s_tree(j, time-ltree[(position, j)]-1, on.union({j}), flow + (time-ltree[(position, j)]-1)*valves[j])

s_tree(start, t, set(), 0)
print(ans)

t: int = 26
ans = -1
i=0
def g_tree(position, time, on: set, flow:int, targets: frozenset):
    delta = 0
    for j in targets.difference(on):
        if ltree[(position, j)] < time-1:
            delta = max(g_tree(j, time-ltree[(position, j)]-1, on.union({j}), flow + (time-ltree[(position, j)]-1)*valves[j], targets), delta)
    return max(delta, flow)

ans = 0

for i in range(2**len(matter)):
    if i % 1000 == 0:
        print(i)

    mtarget = frozenset()
    btarget = frozenset()
    b = bin(i)[2:]
    for j in range(len(b)):
        if b[j] == "1":
            mtarget = mtarget.union({vlist[j]})
        else:
            btarget = btarget.union({vlist[j]})
    x = g_tree(start, t, set(), 0, mtarget)
    y = g_tree(start, t, set(), 0, btarget)
    ans = max(ans, x+y)
print(ans)