from advent import get_input, solution_timer
inp = get_input(2022, 15)

yreq = 2000000
points = {}
pairs = []
for i in inp:
    # pull out sensor location and closest beacon location
    j = i.split(':')
    sensors = j[0].split(' at ')[-1].split(', ')
    x, y = int(sensors[0][2:]), int(sensors[1][2:])
    points[(x, y)] = 0
    beacon = j[1].split(' at ')[-1].split(', ')
    x2, y2 = int(beacon[0][2:]), int(beacon[1][2:])
    points[(x2, y2)] = 0
    # calculate distance between sensor and beacon, manhattan style
    distance = abs(x - x2) + abs(y - y2)
    print(distance)
    # for all points in manhattan distance, add to points dict
    reqy = abs(yreq-y)
    if reqy <= distance:
        for i in range(-(distance - reqy),(distance - reqy)+ 1):
            j = reqy
            if i + j <= distance:
                if (x + i, y + j) not in points:
                    points[(x + i, y + j)] = 1
                if (x - i, y + j) not in points:
                    points[(x - i, y + j)] = 1
                if (x + i, y - j) not in points:
                    points[(x + i, y - j)] = 1
                if (x - i, y - j) not in points:
                    points[(x - i, y - j)] = 1
    print("range added")
    pairs.append((x, y, distance))

ans = 0
for key, val in points.items():
    if key[1] == yreq and val == 1:
        ans += 1
print(ans)


xmin, ymin = 0,0
xmax,ymax = 4000000, 4000000
x = 0
y = 0
ansx = -1
ansy = -1
fans = False
while x < xmax +1:
    #if x % 10000 == 0:
        #print(x)
    y=0
    while y < ymax +1:
        # check that point could not be in range of any sensor
        if fans:
            break
        found = False
        for i in pairs:
            x2,y2, distance = i
            if abs(x2-x) + abs(y2-y) <= distance:
                found = True
                # increment y to the next distance range to check
                if y <= y2:
                    y += 2 * (y2 - y)
                else:
                    y += distance - (y - y2) - abs(x2-x)
                y+=1
                break
        if not found:
            fans = True
            print("found", x, y)

    if fans:
        ansx = x
        ansy = y
        break

    x+=1

print(ansx * 4000000 + y)
