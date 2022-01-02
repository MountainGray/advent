inp = open('2021/day22/ipp.txt').read().split('\n')

points = {}

for i, step in enumerate(inp):
    if i ==20:
        break
    assign = 1 if "on" in step else 0
    a = step.split(" ")[1]
    x,y,z = a.split(",")
    xl, xr = x.replace("x=","").split("..")
    xl, xr = int(xl), int(xr)
    yl, yr = y.replace("y=","").split("..")
    yl, yr = int(yl), int(yr)
    zl, zr = z.replace("z=","").split("..")
    zl, zr = int(zl), int(zr)

    store= 0
    for i in points.values():
        if i == True:
            store+= 1

    for i in range(xl, xr+1):
        for j in range(yl, yr+1):
            for k in range(zl, zr+1):
                points[(i,j,k)] = assign
    summ = 0
    for i in points.values():
        if i == True:
            summ += 1
    print(summ, assign, summ-store)
