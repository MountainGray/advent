from advent import get_input, solution_timer
from collections import Counter

@solution_timer(2018, 2, 1)
def part_one(inp):
    a = 0
    b = 0
    for i in inp:
        c = Counter(i)
        if 2 in c.values():
            a +=1
        if 3 in c.values():
            b +=1
    return a*b

@solution_timer(2018, 2, 2)
def part_two(inp):
    for i in inp:
        for j in inp:
            if i != j:
                x = sum([1 if i[a]!=j[a] else 0 for a in range(len(i))])
                if x == 1:
                    st = ""
                    for a in range(len(i)):
                        if i[a]==j[a]:
                            st+= i[a]
                    return st

            
if __name__ == "__main__":
    input = get_input(2018, 2)
    part_one(input)
    part_two(input)