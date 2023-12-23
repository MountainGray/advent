from advent import get_input, solution_timer, submit
from advent.helpers import *


def get_points(rock):
    return list(product(range(rock[0], rock[3]+1), range(rock[1], rock[4]+1), range(rock[2], rock[5]+1)))

@solution_timer(2023, 22, 1)
def part_one(inp):
    rocks = []

    for line in inp:
        s, e = line.split("~")
        sx, sy, sz = s.split(",")
        ex, ey, ez = e.split(",")
        assert int(sz) <= int(ez)
        assert int(sx) <= int(ex)
        assert int(sy) <= int(ey)
        rocks.append((int(sx), int(sy), int(sz), int(ex), int(ey), int(ez), 0))
    
    conflicts = []
    for i in rocks:
        conflicts += get_points(i)

    while True:

        for idx, i in enumerate(rocks):

            sx, sy, sz, ex, ey, ez, solidified = i

            mp = get_points((sx, sy, sz, ex, ey, ez))

            for p in mp:
                conflicts.remove(p)

            step = True
            while True:
                for x in range(sx, ex+1):
                    for y in range(sy, ey+1):
                        if (x, y, sz-1) in conflicts or sz-1 == 0:
                            step = False
                            break
                    if not step:
                        break
                if step:
                    sz -= 1
                    ez -= 1
                else:
                    break
            

            np = get_points((sx, sy, sz, ex, ey, ez))
            for osx, osy, osz, oex, oey, oez, final in rocks:
                if oez == sz - 1 and final:
                    for x,y,z in get_points((osx, osy, osz, oex, oey, oez)):
                        if (x,y,z+1) in np:
                            solidified = True
                            break
            if sz == 1:
                solidified = True
            rocks[idx] = (sx, sy, sz, ex, ey, ez, solidified)
            conflicts += np

        if all([i[6]==1 for i in rocks]):
            break

    supports = defaultdict(lambda:[])
    for i, r in enumerate(rocks):
        sx, sy, sz, ex, ey, ez, _ = r
        for j, fr in enumerate(rocks):
            if i == j:
                continue
            fsx, fsy, _, fex, fey, fez , _ = fr
            if fez == sz-1:
                if ((sx <= fsx <= ex or sx <= fex <= ex or fsx <= sx <= fex or fsx <= ex<=fex)
                and 
                (sy <= fsy <= ey or sy <= fey <= ey or fsy <= sy <= fey or fsy <= ey<=fey)):
                    supports[i].append(j)
    print(supports)
    print(rocks)
    
    #ans = 0
    #for i in range(len(rocks)):
        #removable = True
        #for j in range(len(rocks)):
            #if j in supports:
                #if supports[j] == [i]:
                    #removable = False
                    #break
        #if removable:
            #ans += 1
    #return ans

    ans = 0
    for i in range(len(rocks)):
        #print(i, ans)
        dp = [i]
        cs = {k:[x for x in v] for k,v in supports.items()}
        #print(cs)
        while len(dp) > 0:
            rem = dp.pop()
            for j in range(len(rocks)):
                if j in cs:
                    if cs[j] == [rem]:
                        #print("removing", j, "as", rem)
                        dp.append(j)
                        ans += 1
                    elif rem in cs[j]:
                        cs[j].remove(rem)
        

    return ans

    ans = 0
    conflicts = []
    for i in rocks:
        conflicts += get_points(i)

    for idx, r in enumerate(rocks):
        print(idx)
        nrocks = rocks[:idx] + rocks[idx+1:]
        mp = get_points(r)
        nconflicts = conflicts[:]
        for p in mp:
            nconflicts.remove(p)

        for i in nrocks:
            sx, sy, sz, ex, ey, ez, _ = i
            step = True
            mp = get_points((sx, sy, sz, ex, ey, ez))
            for p in mp:
                nconflicts.remove(p)
            for x in range(sx, ex+1):
                for y in range(sy, ey+1):
                    if (x, y, sz-1) in nconflicts or sz-1 == 0:
                        step = False
                        break
                if not step:
                    break
            if step:
                ans += 1
            else:
                nconflicts += get_points((sx, sy, sz, ex, ey, ez))

    return ans



@solution_timer(2023, 22, 2)
def part_two(inp):
    pass

if __name__ == "__main__":
    inp = get_input(2023, 22)
    test = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9""".splitlines()
    if test != [""]:
        part_one(test)

    ans = part_one(inp)
    submit(2023, 22, 2, ans)
    exit()

    if test != [""]:
        part_two(test)
    ans = part_two(inp)
    submit(2023, 22, 2, ans)
