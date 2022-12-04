from advent import get_input, solution_timer
import numpy as np

fab = np.zeros((1000,1000))

@solution_timer(2018, 3, 2)
def part_one(inp):
    for i in inp:
        _ , _, chord, rec = i.split()
        x,y = list(map(int,chord[:-1].split(",")))
        a,b = list(map(int, rec.split("x")))
        fab[x:x+a, y:y+b] += 1
    return np.sum(fab > 1)

@solution_timer(2018, 3, 2)
def part_two(inp):
    for i in inp:
        num, _, chord, rec = i.split()
        x,y = list(map(int,chord[:-1].split(",")))
        a,b = list(map(int, rec.split("x")))
        if np.sum(fab[x:x+a, y:y+b] >1)==0:
            return num

if __name__ == "__main__":
    input = get_input(2018, 3)
    part_one(input)
    part_two(input)
