import time
t1=time.perf_counter()
f='Day23/input.txt'
#f='Day23/input2.txt'
fl=open(f).read()
cups=[int(c)for c in fl]
cmax=1000000
cups+=[i for i in range(10,1000001)]
positions={}
for i , num in enumerate(cups[:-1]):
    positions[num]=cups[i+1]
positions[cups[-1]]=cups[0]
current=cups[0]
cmax=max(cups)
turn=0
while True:
    pa=current
    #print('c',current)
    f1=positions[current]
    f2=positions[f1]
    f3=positions[f2]
    f4=positions[f3]
    #print(f1,' ',f2,' ',f3)
    i=1
    while True:
        dest=current-i if current-i>0 else cmax+current-i
        if dest not in [f1,f2,f3]:
            break
        i+=1
    #print('d',dest)
    pastdest=positions[dest]
    positions[current]=f4
    positions[dest]=f1
    positions[f3]=pastdest
    current=positions[current]
    #print()
    if turn==10000000:
        break
    else:
        turn+=1

a1=positions[1]
print(a1)
a2=positions[a1]
print(a2)
print(a1*a2)
t2=time.perf_counter()
print(f'Time: {t2-t1:0.4f} seconds')