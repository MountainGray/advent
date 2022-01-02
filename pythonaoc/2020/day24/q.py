f='Day24/input.txt'
f2='Day24/input2.txt'

lines=open(f).read().splitlines()
n=(0,2)
tiles={}
for line in lines:
    eat=line
    x=0
    y=0
    while True:
        if len(eat)==0:
            break
        elif len(eat)==1: #e or w
            if eat=='e':
                x+=2
            else:
                x-=2
            break
        else:
            if eat[:2]=='ne':
                x+=1
                y+=1
                eat=eat[2:]
            elif eat[:2]=='nw':
                x-=1
                y+=1
                eat=eat[2:]
            elif eat[:2]=='se':
                x+=1
                y-=1
                eat=eat[2:]
            elif eat[:2]=='sw':
                x-=1
                y-=1
                eat=eat[2:]
            elif eat[:1]=='e':
                x+=2
                eat=eat[1:]
            else:
                x-=2
                eat=eat[1:]
    if (x,y) in tiles:
        tiles[(x,y)]+=1
    else:
        tiles[(x,y)]=1

ans=0
for key, val in tiles.items():
    if val%2==1:
        ans+=1
print(ans)
hexmove=[(1,1),(2,0),(1,-1),(-1,1),(-2,0),(-1,-1)]

def expg(dic):
    dcop=dic.copy()
    for key, val in dic.items():
        for dis in hexmove:
            if  (key[0]+dis[0],key[1]+dis[1]) not in dic:
                dcop[(key[0]+dis[0],key[1]+dis[1])]=0
    return dcop
tiles=expg(tiles)
new=tiles.copy()
        

for i in range(100):
    for key, val in tiles.items():
        if val%2==0:#white
            numb=0
            for dis in hexmove:
                if  (key[0]+dis[0],key[1]+dis[1]) in tiles:
                    if tiles[(key[0]+dis[0],key[1]+dis[1])]%2==1:
                        numb+=1
            if numb==2:
                new[key]+=1
        else:#black
            numb=0
            for dis in hexmove:
                if  (key[0]+dis[0],key[1]+dis[1]) in tiles:
                    if tiles[(key[0]+dis[0],key[1]+dis[1])]%2==1:
                        numb+=1
            if numb==0 or numb>2:
                new[key]+=1
    new=expg(new)
    tiles=new.copy()
ans=0
for key, val in tiles.items():
    if val%2==1:
        ans+=1
print(ans)



