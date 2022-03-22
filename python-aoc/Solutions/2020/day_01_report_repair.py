from ..aoc_utils import load_input

inp: list[int] = load_input(2020, 1, map_func=int)

#p1
for i in inp:
    for j in inp:
            if i+j==2020:
                print("P1",i*j)

#p2
for i in inp:
    for j in inp:
        for k in inp:
            if i+j+k==2020:
                print("P2:",i * j * k)