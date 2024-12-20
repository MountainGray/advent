from advent import get_input, solution_timer
from advent.helpers import *

@solution_timer(2024, 19, 1)
def part_one(inp):
    pats, _, *att = inp
    pats = pats.split(", ")
    tried = {"" : True}

    def consume(st):
        if st in tried:
            return tried[st]
        else:
            for pat in pats:
                if st.startswith(pat):
                    if consume(st[len(pat):]):
                        tried[st] = True
                        return True
            tried[st] = False
            return False

    ans = 0
    for i in att:
        if consume(i):
            ans += 1

    return len(list(filter(consume,att)))


@solution_timer(2024, 19, 2)
def part_two(inp):
    pats = inp[0].split(", ")
    att = inp[2:]
    tried = {}

    def consume(st):
        if st in tried:
            return tried[st]
        if st == "":
            return 1 
        else:
            s = 0
            for pat in pats:
                if st.startswith(pat):
                    s += consume(st[len(pat):])
            tried[st] = s
            return s

    return sum(map(consume, att))




if __name__ == "__main__":
    inp = get_input(2024, 19)
    part_one(inp)
    part_two(inp)
