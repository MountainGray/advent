from advent import get_input, solution_timer
from itertools import combinations
import numpy as np
from z3 import Solver, Real, sat


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
        h1px, h1py, h1pz, h1vx, h1vy, h1vz = hail[i]
        h2px, h2py, h2pz, h2vx, h2vy, h2vz = hail[j]
        A = np.array([[h1px, h1py], [h1px + h1vx, h1py + h1vy]])
        B = np.array([[h2px, h2py], [h2px + h2vx, h2py + h2vy]])

        A_diff = A[0] - A[1]
        B_diff = B[0] - B[1]
        div = np.linalg.det([A_diff, B_diff])
        if div == 0:
            continue
        d = (np.linalg.det([A[0], A[1]]) * B_diff - np.linalg.det([B[0], B[1]]) * A_diff) / div
        x, y = d
        if mn <= x <= mx and mn <= y <= mx:
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
    part_one(inp)
    part_two(inp)
