file = open('Day17/input.txt')
lines = file.read().splitlines()
points={}

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        points[(i,j,0)]=True if char=='#'else False

def padGrid(points):
    p2=points.copy()
    for key, val in points.items():
        if val==True:
            for x in (-1, 0, 1):
                for y in (-1, 0, 1):
                    for z in (-1, 0, 1):
                        if  x != 0 or y!=0 or z!=0:
                            if (key[0]+x,key[1]+y,key[2]+z) not in points:
                                p2[(key[0]+x,key[1]+y,key[2]+z)]=False
    return p2

def pgrid(points):
    ma_x=0
    ma_y=0
    ma_z=0
    mi_x=0
    mi_y=0
    mi_z=0
    for key in points.keys():
        ma_x=key[0]if key[0]>ma_x else ma_x
        ma_y=key[1]if key[1]>ma_y else ma_y
        ma_z=key[2]if key[2]>ma_z else ma_z
        mi_x=key[0]if key[0]<mi_x else mi_x
        mi_y=key[1]if key[1]<mi_y else mi_y
        mi_z=key[2]if key[2]<mi_z else mi_z
    for z in range(mi_z,ma_z+1):
        print('z =',z)
        for x in range(mi_x, ma_x+1):
            str=''
            for y in range(mi_y,ma_y+1):
                if (x,y,z) in points:
                    str+= '#' if points[(x,y,z)]==True else '.'
                else:
                    str+=' '
            print(str)
    

        
        

turn=1
prpoints=points.copy()
while True:
    print('turn ',turn)
    pgrid(points)
    points=padGrid(points)
    print(points)
    for point, state in points.items():
        around=0
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                for z in (-1, 0, 1):
                    
                    neighbour=(point[0]+x,point[1]+y,point[2]+z)
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
        

        
        
