from advent import get_input, solution_timer, submit
from advent.helpers import *



from multiprocessing import Pool
def sol(i, instrs):
    vs = { "A" : i, "B" : 0, "C" : 0 }

    ip = 0
    out = []
    while ip < len(instrs):
        js = False
        op, rand = instrs[ip:ip+2]

        lp = rand

        if rand <=3:
            combo = rand
        if rand == 4:
            combo = vs["A"]
        if rand == 5:
            combo = vs["B"]
        if rand == 6:
            combo = vs["C"]

        match op:
            case 0:
                num = vs["A"]
                denom = 2**combo
                vs["A"] = num // denom
            case 1:
                vs["B"] = vs["B"] ^ lp
            case 2:
                vs["B"] = combo % 8
            case 3:
                if vs["A"] != 0:
                    js = True
                    ip = lp
            case 4:
                vs["B"] = vs["B"] ^ vs["C"]
            case 5:
                out += [combo % 8]
                lout = len(out)
                if out != instrs[:lout]:
                    return False
                #print(f"{combo % 8},", end="")
            case 6:
                num = vs["A"]
                denom = 2**combo
                vs["B"] = num // denom
            case 7:
                num = vs["A"]
                denom = 2**combo
                vs["C"] = num // denom
        if not js:
            ip += 2
    if out == instrs:
        return True

def search_range(inp):
    rng, instrs = inp
    for i in range(rng[0], rng[1]):
        # if i % 10000000 == 0:
        #     print(i)
        if sol(i, instrs):
            print(f"Found it {i}")
            return i
    #print("D")
    return 0

@solution_timer(2024, 17, 1)
def part_one(inp: list[str]):
    # Register A: 33940147
    # Register B: 0
    # Register C: 0
    instrs = inp
    
    #for i in range(33940147, 1000000000000):
    # for i in range(1000000000000):
    #     if i % 1000000 == 0:
    #         print(i)
    #     if sol(i, instrs):
    #         return i
    with Pool(12) as p:
        ranges = [((i, i+1000000),instrs) for i in range(0, 1000000000000, 1000000)]
        print(len(ranges))
        vals = p.map(search_range, ranges)
        print("DONE")
        print(vals)
        v = [i for i in vals if i != 0]
        return v[0]
    #     p.map(sol, range(33940147, 1000000000000)))


# 31050000


@solution_timer(2024, 17, 2)
def part_two(inp: list[str]):
    pass

if __name__ == "__main__":
    inp = get_input(2024, 17, split_char="\n\n")
    # ans = part_one([int(i) for i in "0,3,5,4,3,0".split(",")])
    # print(ans)
    ans = part_one([int(i) for i in "2,4,1,5,7,5,1,6,4,2,5,5,0,3,3,0".split(",")])
    submit(2024, 17, 2, ans)
    #part_two(inp)
