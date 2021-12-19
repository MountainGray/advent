inp = open('2021/day19/input.txt').read().split('\n\n')
class scanr:
    def __init__(self, num, points) -> None:
        self.num = num
        self.points = points
        self.locked = False
        self.translation = [0,0,0]
    
    def translate(self, translation):
        trans = lambda x, y, z: [x+translation[0], y+translation[1], z+translation[2]]
        for i in range(len(self.points)):
            self.points[i] = trans(*self.points[i])
    
    def rotate(self, axis):
        for i in range(len(self.points)):
            if axis == 0:
                self.points[i] = [self.points[i][0], -self.points[i][2], self.points[i][1]]
            if axis == 1:
                self.points[i] = [self.points[i][2], self.points[i][1], -self.points[i][0]]
            if axis == 2:
                self.points[i] = [-self.points[i][1], self.points[i][0], self.points[i][2]]
nodes = []
for chunk in inp:
    chunk = chunk.split("\n")
    node = int(chunk[0][12:-4])
    points = []
    for pointpair in chunk[1:]:
        x,y,z = map(int,pointpair.split(","))
        points.append([x,y,z])
    nodes.append(scanr(node,points))

def match_list(a:scanr,b:scanr):
    for _ in range(3):
        for _ in range(4):
            for _ in range(4):
                for pa in a.points:
                    for pb in b.points:
                        match = 0
                        trns = [pa[0]-pb[0], pa[1]-pb[1], pa[2]-pb[2]]
                        for tb in b.points:
                            if [tb[0]+trns[0], tb[1]+trns[1], tb[2]+trns[2]] in a.points:
                                match+=1
                        if match>=3:
                            print("foundmatch")
                            b.locked = True
                            b.translate(trns)
                            b.translation = trns
                            return True
                b.rotate(0)
            b.rotate(1)
        b.rotate(2)
    return False
locked = [nodes[0]]
locked[0].locked=True
while True:
    for s in locked:
        for node in nodes:
            if node.locked == True:
                continue
            elif node.num == s.num:
                continue
            else:
                if match_list(s, node):
                    node.locked=True
                    locked.append(node)
    if len(nodes) ==len(locked):
        break
print(len(set([tuple(point)for node in locked for point in node.points])))
ma= 0
for n1 in locked:
    for n2 in locked:
        mh = abs(n1.translation[0] - n2.translation[0]) + abs(n1.translation[1] - n2.translation[1]) + abs(n1.translation[2] - n2.translation[2])
        ma = mh if mh > ma else ma
print(ma)

