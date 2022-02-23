f='Day23/input.txt'
#f='Day23/input2.txt'
fl=open(f)
line=fl.read()
print(line)
cups=[int(c)for c in line]
cups+=[i for i in range(10,1000001)]
cmax=max(cups)
turn=0
current=cups[0]
while True:
    cindex=cups.index(current)
    selection=[cups.pop((cindex+1)if cindex+1<len(cups)else 0) for i in range(3)]
    destination=current-1
    if destination==0:
        destination=cmax
    while destination in selection:
        destination-=1
        if destination==0:
            destination=cmax
    dindex=cups.index(destination)
    cups=cups[:dindex+1]+selection+cups[dindex+1:]
    cindex=cups.index(current)
    current=cups[(cindex+1)%len(cups)]
    turn+=1
    if turn%500==0:
        print('turn')
    if turn==10000001:

        break
