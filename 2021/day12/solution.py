inp = open('2021/day12/input.txt').read().split('\n')
connections: dict[str, list[str]]= {}

for line in inp:
    a, b = line.split("-")
    if a not in connections: connections[a] = []
    if b not in connections: connections[b] = []
    connections[a].append(b)
    connections[b].append(a)

def findpath(position, path, double, doubled):
    if position == "end":
        return 1
    below = 0
    for next in connections[position]:
        if next not in path or next.isupper() or (double and next.islower() and not doubled and not next == "start"):
            if next.islower() and next in path:
                below += findpath(next, path + [next], double, True)
            else:
                below += findpath(next, path + [next], double, doubled)
            doubled = False
    return below

print("P1:",findpath("start", ['start'] , False , False))
print("P2:",findpath("start", ['start'] , True, False))