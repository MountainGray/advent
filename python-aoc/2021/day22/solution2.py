inp = open('2021/day22/input.txt').read().split('\n')

class cube:
    def __init__(self, xl, xr, yl, yr, zl, zr, state):
        self.xl = xl
        self.xr = xr
        self.yl = yl
        self.yr = yr
        self.zl = zl
        self.zr = zr
        self.state = state
        self.volume = (xr+1-xl)*(yr+1-yl)*(zr+1-zl)
    
    def __repr__(self) -> str:
        return f"cube({self.xl},{self.xr},{self.yl},{self.yr},{self.zl},{self.zr},{self.state}, {self.volume})"

poscubes = []
for i, step in enumerate(inp):
    assign = 1 if "on" in step else 0
    a = step.split(" ")[1]
    x,y,z = a.split(",")
    xl, xr = x.replace("x=","").split("..")
    xl, xr = int(xl), int(xr)
    yl, yr = y.replace("y=","").split("..")
    yl, yr = int(yl), int(yr)
    zl, zr = z.replace("z=","").split("..")
    zl, zr = int(zl), int(zr)
    cub = cube(xl, xr, yl, yr, zl, zr, assign)
    poscubes.append(cub)

def get_ol(old_cube, new_cube):
    xl, xr, yl, yr, zl, zr = new_cube.xl, new_cube.xr, new_cube.yl, new_cube.yr, new_cube.zl, new_cube.zr
    oxl, oxr, oyl, oyr, ozl, ozr = old_cube.xl, old_cube.xr, old_cube.yl, old_cube.yr, old_cube.zl, old_cube.zr
    overlap = max(min(xr,oxr)+1-max(xl,oxl), 0) * max(min(yr,oyr)+1-max(yl,oyl), 0) * max(min(zr,ozr)+1-max(zl,ozl), 0)
    return overlap

def get_intersection_cube(c1, c2):
    xl, xr, yl, yr, zl, zr = c1.xl, c1.xr, c1.yl, c1.yr, c1.zl, c1.zr
    oxl, oxr, oyl, oyr, ozl, ozr = c2.xl, c2.xr, c2.yl, c2.yr, c2.zl, c2.zr
    overlap = max(min(xr,oxr)+1-max(xl,oxl), 0) * max(min(yr,oyr)+1-max(yl,oyl), 0) * max(min(zr,ozr)+1-max(zl,ozl), 0)
    if overlap>0:
        return cube(max(xl,oxl), min(xr,oxr), max(yl,oyl), min(yr,oyr), max(zl,ozl), min(zr,ozr), True)
    else:
        return None

def get_above(i, cub, sign):
    volume = 0
    for j in range(i+1, len(poscubes)):
        overlap = get_intersection_cube(cub, poscubes[j])
        if overlap==None: continue
        volume+= get_above(j, overlap, 1-sign)
        if sign:
            volume -= get_ol(overlap,poscubes[i],)
        else:
            volume += get_ol(overlap,poscubes[i] )
    return volume

total = 0
for i, cub in enumerate(poscubes):
    if cub.state == 1:
        total += cub.volume + get_above(i, cub, 1)


print(total)
print(2758514936282235)


