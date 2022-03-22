from typing import Counter
from copy import deepcopy
file = open('Day11/input2.txt', 'r')
lines=file.read().splitlines()
plane=[]
for line in lines:
    row=[]
    for char in line:
        row.append(char)
    plane.append(row)
for i,lin in enumerate(plane):
    for j, ch in enumerate(lin):
        if ch=='L':
            plane[i][j]='#'
planewid=len(lines[0])
planeleng=len(lines)
plane2=deepcopy(plane)

plane_old=deepcopy(plane)
while True:
    for i, lin in enumerate(plane):
        for j, ch in enumerate(lin):
            if ch=='L':
                space=True
                for k in range(i-1,i+2):
                    for l in range(j-1,j+2):
                        if -1<k and k<planeleng and -1<l and l<planewid:
                            if plane_old[k][l]=="#":
                                space=False
                if space==True:
                    plane[i][j]='#'
            elif ch=='#':
                leave=0
                for k in range(i-1,i+2):
                    for l in range(j-1,j+2):
                        if -1<k and k<planeleng and -1<l and l<planewid:
                            if plane_old[k][l]=="#":
                                if k==i and l==j:
                                    continue
                                else:
                                    leave+=1
                if leave>=4:
                    plane[i][j]='L'
    if plane_old==plane:
        break
    plane_old=deepcopy(plane)
empty=0
for line in plane:
    for seat in line:
        if seat=="#":
            empty+=1
print(empty)

#part 2
old_plane2=deepcopy(plane2)
while True:
    print('\n')
    for i, lin in enumerate(plane2):
        for j, ch in enumerate(lin):
            if ch=='L':
                space=True
                for k in (-1,0,1):
                    for l in (-1,0,1):
                        range=1
                        while True:
                            if k==0 and l==0:
                                break
                            elif -1<i+k*range and i+k*range<planeleng and -1<j+l*range and j+l*range<planewid:
                                if old_plane2[i+k*range][j+l*range]=="#":
                                    space=False
                                    break
                                else:
                                    range+=1
                            else:
                                break
                if space==True:
                    plane2[i][j]='#'
            elif ch=='#':
                leave=0
                for k in (-1,0,1):
                    for l in (-1,0,1):
                        range=1
                        while True:
                            if k==0 and l==0:
                                break
                            elif -1<i+k*range and i+k*range<planeleng and -1<j+l*range and j+l*range<planewid:
                                if old_plane2[i+k*range][j+l*range]=="#":
                                    leave+=1
                                    break
                                range+=1
                            else:
                                break
                if leave>=5:
                    plane2[i][j]='L'
    
    for line in plane2:
        print(line)
    if old_plane2==plane2:
        break
    old_plane2=deepcopy(plane2)
empty=0
for line in plane2:
    for seat in line:
        if seat=="#":
            empty+=1
print(empty)