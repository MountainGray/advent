file = open('Day17/input.txt')
lines = file.read().splitlines()
points={}

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        points[(i,j,0,0)]=True if char=='#'else False

def padGrid(points):
    p2=points.copy()
    for key, val in points.items():
        if val==True:
            for x in (-1, 0, 1):
                for y in (-1, 0, 1):
                    for z in (-1, 0, 1):
                        for w in (-1,0,1):
                            if  x != 0 or y!=0 or z!=0 or w!=0:
                                if (key[0]+x,key[1]+y,key[2]+z, key[3]+w) not in points:
                                    p2[(key[0]+x,key[1]+y,key[2]+z,key[3]+w)]=False
    return p2

turn=1
prpoints=points.copy()
while True:
    print('turn ',turn)
    points=padGrid(points)
    for point, state in points.items():
        around=0
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                for z in (-1, 0, 1):
                    for w in (-1,0,1):
                        neighbour=(point[0]+x,point[1]+y,point[2]+z,point[3]+w)
                        if neighbour in prpoints and neighbour!= point:
                            if prpoints[neighbour]==True:
                                around+=1
        if state==True:
            if around<2 or around >3:
                points[point]=False
        else:
            if around==3:
                points[point]=True

    if turn==6:
        break
    turn+=1
    prpoints=points.copy()

ans=0
for key, val in points.items():
    if val==True:
        ans+=1

print(ans)
        

        
        
