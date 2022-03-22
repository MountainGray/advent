from copy import deepcopy
inp = open('2021/day24/input.txt').read().split('\n')
insp = []
for i, cal in enumerate(inp):
    if "inp" in cal:
        insp.append(i)

pchunks = []
for i in range(13):
    pchunks.append(inp[insp[i]:insp[i+1]])
pchunks.append(inp[insp[-1]:])


for i 

memo = {}
def process(instructions:list, num:int, iw,ix,iy,iz):
    struc = deepcopy(instructions)
    w,x,y,z = iw,ix,iy,iz
    kw = {
        "w":w,
        "x":x,
        "y":y,
        "z":z,
    }
    def parse(i):
        if i in ["x", "y","z","w"]:
            return kw[i]
        else:
            return int(i)

    while len(struc)!=0:
        inst = struc.pop(0)
        inst = inst.split(" ")
        if inst[0]=="inp":
            kw[inst[1]]=num
        if inst[0]=="add":
            kw[inst[1]]=kw[inst[1]] + parse(inst[2])
        if inst[0]=="mul":
            kw[inst[1]]=kw[inst[1]] * parse(inst[2])
        if inst[0]=="div":
            if parse(inst[2])==0:
                continue
            kw[inst[1]]=parse(inst[1]) // parse(inst[2])
        if inst[0]=="mod":
            if kw[inst[1]]<0 or parse(inst[2])<=0:
                continue
            kw[inst[1]]=kw[inst[1]] % parse(inst[2])
        if inst[0]=="eql":
            kw[inst[1]]= 1 if kw[inst[1]] == parse(inst[2]) else 0
    return kw["w"], kw["x"],kw["y"],kw["z"]




def main():
    start = 99999999999999
    def recur(i, str, w,x,y,z):
        ow,ox,oy,oz = w,x,y,z
        cnum = int(str[i])
        nchunk = pchunks[i]
        #print((i,str[i:],ow,ox,oy,oz))
        if (i,str[i:],ow,ox,oy,oz) not in memo:
            nw,nx,ny,nz = process(nchunk, cnum,ow,ox,oy,oz)
            if i < 13:
                rcur = recur(i+1,str,nw,nx,ny,nz)
                memo[(i,str[i:],ow,ox,oy,oz)]= rcur
                return rcur
            else:
                memo[(i,str[i:],ow,ox,oy,oz)] = nw,nx,ny,nz
                return [nw,nx,ny,nz]
        else:
            return memo[(i,str[i:],ow,ox,oy,oz)]

    while True:
        stcheck = str(start)
        if "0" not in stcheck:
            w,x,y,z = 0,0,0,0
            nw,nx,ny,nz = recur(0,stcheck,w,x,y,z)
            if nz == 0:
                print(stcheck)
                break
        start -= 1

#main()
