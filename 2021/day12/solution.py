inp = open('2021/day12/input.txt').read().split('\n')
connections: dict[str, list[str]]= {}

for line in inp:
    a, b = line.split("-")
    if a not in connections: connections[a] = []
    if b not in connections: connections[b] = []
    connections[a].append(b)
    connections[b].append(a)

def findpath(position, path, double):
    if position == "end":
        return 1
    below = 0
    for next in connections[position]:
        if next not in path or next.isupper() or (double and next.islower() and not doublelittle(path) and not next == "start"):
            np = path + [next]
            below += findpath(next, np, double)
    return below

def doublelittle(list):
    ss = set(list)
    for i in ss:
        if i.islower() and list.count(i) == 2:
            return True
    return False

print("P1:",findpath("start", ['start'] , False))
print("P2:",findpath("start", ['start'] , True))