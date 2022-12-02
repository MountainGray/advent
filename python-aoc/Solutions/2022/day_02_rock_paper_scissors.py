from advent import get_input, solution_timer

translate = {"X": "A", "Y": "B", "Z": "C"}
point = {"A": 1, "B": 2, "C": 3}
beats = {"A":"C", "B":"A", "C":"B"}
beater = dict(reversed(list(beats.items())))

@solution_timer(2022, 2, 1)
def part_one(inp):
    ans = 0
    for a, b in [x.split(" ") for x in inp]:
        ans += point[translate[b]]
        if translate[b]==beats[a]: ans +=0
        elif a== translate[b]: ans += 3
        else: ans += 6
    return ans

@solution_timer(2022, 2, 2)
def part_two(inp):
    ans = 0
    for a, b in [x.split(" ") for x in inp]:
        if b == "X": ans += point[beats[a]]
        elif b == "Y": ans += 3 + point[a]
        else: ans += 6 + point[beater[a]]
    return ans

if __name__ == '__main__':
    inp = get_input(2022, 2)
    part_one(inp)
    part_two(inp)