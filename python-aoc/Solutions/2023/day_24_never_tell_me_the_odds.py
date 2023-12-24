from advent import get_input, solution_timer
from itertools import combinations
from z3 import *


mn = 200000000000000
mx = 400000000000000
@solution_timer(2023, 24, 1)
def part_one(inp):
    hail = []
    for line in inp:
        pos, vel = line.split(" @ ")
        px, py, pz = [int(x) for x in pos.split(", ")]
        vx, vy, vz = [int(x) for x in vel.split(", ")]
        hail.append([px, py, pz, vx, vy, vz])

    ans = 0 
    for i, j in combinations(range(len(hail)), 2):
        print(i, j)
        h1px, h1py, h1pz, h1vx, h1vy, h1vz = hail[i]
        h2px, h2py, h2pz, h2vx, h2vy, h2vz = hail[j]
        s = Solver()
        t = Real("t")
        s.add(t >= 0)
        s.add(h1px + h1py + h1vx*t + h1vy*t == h2px + h2py + h2vx*t + h2vy*t)
        if s.check() == sat:
            t = s.model()[t]
            print(t)
            t = t.as_decimal(prec=10)
            print(t)
            if mn <= h1px + h1vx*t <= mx and mn <= h1py + h1vy*t <= mx:
                ans += 1
    return ans


@solution_timer(2023, 24, 2)
def part_two(inp):
    hail = []
    for line in inp:
        pos, vel = line.split(" @ ")
        px, py, pz = [int(x) for x in pos.split(", ")]
        vx, vy, vz = [int(x) for x in vel.split(", ")]
        hail.append([px, py, pz, vx, vy, vz])

    mpy = Real("mpy")
    mpx = Real("mpx")
    mpz = Real("mpz")
    mvx = Real("mvx")
    mvy = Real("mvy")
    mvz = Real("mvz")
    s = Solver()

    for idx, hl in enumerate(hail):
        t = Real(f"t{idx}")
        s.add(t >= 0)
        px, py, pz, vx, vy, vz = hl
        s.add(px + vx*t == mpx + mvx*t)
        s.add(py + vy*t == mpy + mvy*t)
        s.add(pz + vz*t == mpz + mvz*t)
    s.check()
    mpx = s.model()[mpx].as_long()
    mpy = s.model()[mpy].as_long()
    mpz = s.model()[mpz].as_long()
    return mpx + mpy + mpz

if __name__ == "__main__":
    inp = get_input(2023, 24)
    #part_one(inp)
    part_two(inp)
