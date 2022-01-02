xl, xh, yl, yh, top, count= 235, 259, -118, -62, 0,0
for i in range(260):
    for j in range(yl, 118):
        x, y, vx, vy, rm = 0, 0, i, j, 0
        while True:
            x, y = x + vx, y + vy
            if vx > 0: vx -= 1
            vy -= 1
            rm = max(y, rm)
            if xl <= x and x <= xh and yl <= y and y <= yh:
                top, count = max(rm, top), count + 1
                break
            elif x > xh or y < yl:
                break
print(top, count)
