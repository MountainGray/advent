file=open('Day16/input.txt')
lines=file.read().splitlines()

totaltickets=len(lines[25:])
fields={}
for i in lines[:20]:
    two=i.split(': ')
    rng=two[1].split(' or ')
    r1=rng[0].split('-')
    r1=[int(r1[0]),int(r1[1])]
    r2=rng[1].split('-')
    r2=[int(r2[0]),int(r2[1])]
    fields[two[0]]=[r1,r2]

errorate=0
tickets=lines[25:]

for i in lines[25:]:
    vals=i.split(',')
    valtick=True
    for j in vals:
        out=True
        val=int(j)
        for key,k in fields.items():
            for rng in k:
                if rng[0]<=val and rng[1]>=val:
                    out=False
        if out==True:
            errorate+=val
            valtick=False
    if valtick==False:
        tickets.remove(i)

listtickets=[]
for i in tickets:
    nums=i.split(',')
    listtickets.append([int(j) for j in nums])
listtickets.append([int(i) for i in lines[22].split(',')])

print(errorate)
positionsposs={}
for key, ranges in fields.items():
    m=0
    while True:
        passes=True
        for i in listtickets:
            if (ranges[0][0]>i[m]or ranges[0][1]<i[m]) and (ranges[1][0]>i[m] or ranges[1][1]<i[m]):
                passes=False
                break
        if passes==False:
            m+=1
            if m>19:
                break
        else:
            if key not in positionsposs:
                positionsposs[key]=[m]
            else:
                positionsposs[key].append(m)
            m+=1
            if m>19:
                break

finalpos={}
taken=[]
sortedposs=sorted(positionsposs, key = lambda key: len(positionsposs[key]))
for i in sortedposs:
    for j in positionsposs[i]:
        if j not in taken:
            finalpos[i]=j
            taken.append(j)

finalans=1
for key,val in finalpos.items():
    if 'departure'in key:
        finalans*=listtickets[-1][val]
print(finalans)


                    

                    
