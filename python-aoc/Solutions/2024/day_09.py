from advent import get_input, solution_timer
from advent.helpers import *

@solution_timer(2024, 9, 1)
def part_one(inp: list[str]):
    inp= [int(x) for x in inp[0]]
    ans = 0
    maps= []
    i = 0
    mappings = {}
    holes = []
    map = []
    for idx, c in enumerate(inp):
        v=  int(c)
        if idx%2 ==0:
            for _ in range(v):
                if holes:
                    x = holes.pop(0)
                    map[x] = i
                else:
                    map.append(i)
            i+=1
        else:
            for _ in range(v):
                holes.append(len(map)-1)
                maps.append(0)



    return sum([i * map[i] for i in range(len(map))])

@solution_timer(2024, 9, 2)
def part_two(inp: list[str]):
    inp= [int(x) for x in inp[0]]
    ans = 0
    maps= {}
    maps= []
    i = 0
    mappings = {}
    holes = []
    for idx, c in enumerate(inp):
        v=  int(c)
        if idx%2 ==0:
            mappings[i] = (len(maps), len(maps) + v -1)

            for _ in range(v):
                maps.append(i)
            i+=1
        else:
            holes.append((len(maps), len(maps) + v -1))
            for _ in range(v):
                maps.append(-1)

    for i in range(i-1,0,-1):
        holes = sorted(holes, key=lambda x: x[0])
        sp, ep = mappings[i]
        for idx, (hl,hr) in enumerate(holes):
            if (hr-hl) >= ep-sp and hl < sp:
                holes.append((sp,ep))
                holes.remove((hl,hr))
                d = ep-sp
                mappings[i] = (hl, hl + d)
                if hl +d < hr:
                    holes.append((hl+d+1, hr))
                break

    for k,v in mappings.items():
        print(k,v)
        sp, ep =v 
        for i in range(sp, ep + 1):
            ans += k * i

    return ans

        

if __name__ == "__main__":
    inp = """12345""".splitlines()
    inp = """2333133121414131402""".splitlines()
    inp = get_input(2024, 9, split_char="\n")
    part_one(inp)
    # part_two(inp)
