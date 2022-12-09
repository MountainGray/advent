from advent import get_input, submit
inp = get_input(2022, 9)
#inp = """R 4
#U 4
#L 3
#D 1
#R 4
#D 1
#L 5
#R 2""".splitlines()

visited = {(0, 0)}
#xh, yh = 0,0 
#xt, yt = 0,0

points = [[0, 0] for i in range(10)]
for i in inp:
    i = i.split()
    d, dist = i[0], int(i[1])
    for i in range(dist):
        if d == "D":    
            points[0][1] -= 1
        if d == "U":    
            points[0][1] += 1
        if d == "L":    
            points[0][0] -= 1
        if d == "R":    
            points[0][0] += 1
        # drag tail
        for j in range(1, len(points)):
            xh, yh = points[j-1]
            xt, yt = points[j]
            if (abs(xt-xh) >1 and yt==yh):
                if xt > xh:
                    points[j][0] -= 1
                else:
                    points[j][0] += 1
            elif (abs(yt-yh) >1 and xt==xh):
                if yt > yh:
                    points[j][1] -= 1
                else:
                    points[j][1] += 1
            elif (abs(xt-xh) >=1 and abs(yt-yh) >1) or (abs(xt-xh) >1 and abs(yt-yh) >=1):
                if xt>xh:
                    points[j][0] -= 1
                elif xt<xh:
                    points[j][0] += 1
                
                if yt>yh:
                    points[j][1] -= 1
                elif yt<yh:
                    points[j][1] += 1
            if j == len(points)-1:
                visited.add((xt, yt))
        

print(len(visited))

#submit(2022, 9, 1, ans)
#submit(2022, 9, 2, ans)