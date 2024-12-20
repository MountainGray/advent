from advent import get_input
from z3 import *

gn = re.compile(r"\d+")

def part1(inp: list[str]):
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


def part2(inp: list[str]):
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

if __name__ == "__main__":
    inp = get_input(2024, 13, split_char="\n\n")
    part1(inp)
    part2(inp)
