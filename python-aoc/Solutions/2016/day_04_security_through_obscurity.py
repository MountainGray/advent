# Security Through Obscurity
from advent import get_input, solution_timer
from advent.helpers import *

@solution_timer(2016, 4, 1)
def part_one(inp):
    ans = 0
    for x in inp:
        name, cs = x.split("[")
        cs = cs[:-1]
        vals = name.split("-")
        id_vl = int(vals[-1])
        letters = "".join(vals[:-1])
        print(list(letters))
        c = Counter(list(letters))
        print(c.most_common())
        
        tcs = "".join([x[0] for x in sorted(c.items(), key=lambda x: (-x[1], x[0]))[:5]])
        print(tcs, cs)
        if cs == tcs:
            ans += id_vl 
    return ans


        
        


@solution_timer(2016, 4, 2)
def part_two(inp):
    ans = 0
    for x in inp:
        name, cs = x.split("[")
        cs = cs[:-1]
        vals = name.split("-")
        id_vl = int(vals[-1])
        vals = "".join(vals[:-1])
        ns = []
        for x in vals:
            ns.append(rot_chr(x, id_vl))
        ns = "".join(ns)
        if "north" in ns:
            return id_vl

            

if __name__=="__main__":
    inp = get_input(2016, 4, split_char="\n")
    # inp = ["qzmt-zixmtkozy-ivhz-343[abxyz]"]
    # inp= ["aaaaa-bbb-z-y-x-123[abxyz]",
    #       "a-b-c-d-e-f-g-h-987[abcde]",
    #       "not-a-real-room-404[oarel]",
    #       "totally-real-room-200[decoy]"]
    # part_one(inp)
    part_two(inp)
