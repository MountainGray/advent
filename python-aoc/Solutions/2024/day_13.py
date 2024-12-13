#from advent import get_input, solution_timer, submit
# from advent.helpers import *
# import sympy as sp
from z3 import *

gn = re.compile(r"\d+")
inp = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""".split("\n\n")
inp = get_input(2024, 13, split_char="\n\n")



for eq in inp:
    a,b,c = eq.splitlines()
    ax,ay = gn.findall(a)
    bx,by = gn.findall(b)
    tx, ty = gn.findall(c)
    s= Optimize()
    a = Int("a")
    b = Int("b")
    s.add(a <= 100)
    s.add(a >= 0)
    s.add(b <= 100)
    s.add(b >= 0)
    s.add(a* ax + b  * bx == tx)
    s.add(a* ay + b  * by == ty)
    s.minimize(a)
    if s.check() == "sat":
        print(s.model())



    exit()
# submit(2024, 13, 1, ans)
# submit(2024, 13, 2, ans)
