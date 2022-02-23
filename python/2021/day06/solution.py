dist = [0 for _ in range(9)]
for fish in [int(i) for i in open('2021/day06/input.txt').read().split(',')]: dist[fish] += 1
for i in range(256): dist[(i+7)%9] += dist[i%9]
print(sum(dist))
