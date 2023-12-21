from advent import get_input, solution_timer
from advent.helpers import defaultdict

low = 0
high = 1
start = "broadcaster"
@solution_timer(2023, 20, 1)
def part_one(inp):
    maps = {}
    cinps = {}
    for line in inp:
        key, cons = line.split(" -> ")
        if "%" in key or "&" in key:
            t = key[0]
            key = key[1:]
        else:
            t = "start"

        cons = cons.split(", ")
        for con in cons:
            if con not in cinps:
                cinps[con] = {}
            cinps[con][key] = low
        state = (0,t, cons)
        maps[key] = state 

    lc, hc = 1000, 0

    for _ in range(1000):
        _, t, cons = maps[start]
        signals = [(low, x, start) for x in cons]
        while len(signals) > 0:
            level, target, src = signals.pop(0)
            if target == "rx":
                continue
            if level == low:
                lc += 1
            else:
                hc += 1
            cstate, ctype, ccons = maps[target]
            match ctype:
                case "%":
                    if level == high:
                        continue
                    if cstate == low:
                        cstate = high
                        for con in ccons:
                            signals.append((high, con, target))
                    else:
                        cstate = low
                        for con in ccons:
                            signals.append((low, con, target))
                case "&":
                    cinps[target][src] = level
                    if all(cinps[target].values()):
                        for con in ccons:
                            signals.append((low, con, target))
                    else:
                        for con in ccons:
                            signals.append((high, con, target))
                case _:
                    continue
            maps[target] = (cstate, ctype, ccons)
        
    print(lc, hc)
    return lc * hc



                    






@solution_timer(2023, 20, 2)
def part_two(inp):
    maps = {}
    cinps = {}
    for line in inp:
        key, cons = line.split(" -> ")
        if "%" in key or "&" in key:
            t = key[0]
            key = key[1:]
        else:
            t = "foo"

        cons = cons.split(", ")
        for con in cons:
            if con not in cinps:
                cinps[con] = {}
            cinps[con][key] = low
        state = (0,t, cons)
        maps[key] = state 


    lc, hc = 1000, 0

    maps["rx"] = (low, "foo", [])
    maps["output"] = (low, "foo", [])
    tff = defaultdict(int)
    itv = defaultdict(int)

    i = 0
    while True:
        i += 1
        _, t, cons = maps[start]
        signals = [(low, x, start) for x in cons]
        rxc = 0
        while len(signals) > 0:
            level, target, src = signals.pop(0)
            if target == "rx":
                if level == low:
                    return i
                else:
                    rxc += 1
            #print(level, target, src)
            if level == low:
                lc += 1
            else:
                hc += 1
            cstate, ctype, ccons = maps[target]
            match ctype:
                case "%":
                    if level == high:
                        continue
                    if cstate == low:
                        cstate = high
                        for con in ccons:
                            signals.append((high, con, target))
                    else:
                        cstate = low
                        for con in ccons:
                            signals.append((low, con, target))
                case "&":
                    cinps[target][src] = level
                    if all(cinps[target].values()):
                        for con in ccons:
                            signals.append((low, con, target))
                    else:
                        for con in ccons:
                            signals.append((high, con, target))
                    if target == "sq" and level == high:
                        #print(src, i-tff[src])
                        itv[src] = i - tff[src]
                        if all([itv[x] > 0 for x in ["fv", "kk", "vt", "xr"]]):
                            print(itv)
                            from math import lcm
                            return lcm(*itv.values())
                        tff[src] = i


                case _:
                    continue
            maps[target] = (cstate, ctype, ccons)






        

if __name__ == "__main__":
    inp = get_input(2023, 20)
    part_one(inp)
    part_two(inp)
