from advent import get_input

inp = get_input(2022, 20)

positions = {}

vals = [int(i)*811_589_153 for i in inp]
for i in range(1,len(vals)-1):
    positions[(vals[i],i)] = ((vals[i-1],i-1),(vals[i+1],i+1))
positions[(vals[0],0)] = ((vals[-1],len(vals)-1),(vals[1],1))
positions[(vals[-1],len(vals)-1)] = ((vals[-2],len(vals)-2),(vals[0],0))

def imod(num):
    return abs(num)%(len(vals)-1)


for _ in range(10):
    for idx, i in enumerate(vals):
        i=(i,idx)
        behind, ahead = positions[i]
        if i[0]==0:
            continue
        elif  i[0] > 0:
            positions[behind] = (positions[behind][0], ahead)
            positions[ahead] = (behind, positions[ahead][1])

            interval = i[0]%len(positions)
            for j in range(imod(i[0])):
                ahead = positions[ahead][1]
            behind = positions[ahead][0]
            positions[i] = (behind, ahead)
            positions[behind] = (positions[behind][0], i)
            positions[ahead] = (i, positions[ahead][1])
        else:
            positions[behind] = (positions[behind][0], ahead)
            positions[ahead] = (behind, positions[ahead][1])
            for j in range(imod(i[0])):
                behind= positions[behind][0]
            ahead = positions[behind][1]
            positions[i] = (behind, ahead)
            positions[behind] = (positions[behind][0], i)
            positions[ahead] = (i, positions[ahead][1])

nl = []
target = (0, vals.index(0))
nl.append(target[0])
for i in range(len(positions)-1):
    target = positions[target][1]
    nl.append(target[0])
#print(nl[0], nl[-1])
ans = 0
target = (0, vals.index(0))
for i in range(1000):
    target = positions[target][1]
ans += target[0]
for i in range(1000):
    target = positions[target][1]
ans += target[0]
for i in range(1000):
    target = positions[target][1]
ans += target[0]
print(ans)
print("way2")
ml = len(nl) 
n1 = nl[1000%ml]
n2 = nl[2000%ml]
n3 = nl[3000%ml]
print(n1,n2,n3)
print(n1+n2+n3)


