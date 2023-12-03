from advent import get_input, solution_timer
from advent.helpers import defaultdict

@solution_timer(2023, 3, 1)
def part_one(inp):
    y_dim, x_dim = len(inp), len(inp[0])
    inp = defaultdict(lambda: '.', {(x,y): c for y, line in enumerate(inp) for x, c in enumerate(line)})
    ans = 0
    csum = 0
    group = False
    valid = False
    for y in range(y_dim):
        for x in range(x_dim):
            val = inp[(x,y)]
            if val.isnumeric():
                csum = csum * 10 + int(val)
                group = True
                if not valid:
                    # look in nearby cells for for a symbol
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if inp[(x+i,y+j)] != '.' and not inp[(x+i,y+j)].isnumeric():
                                valid = True
                                break
                        if valid:
                            break
            else: # mid line char
                if group:
                    if valid:
                        ans += csum
                    group = False
                    valid = False
                    csum = 0
        # end of line
        if group:
            if valid:
                ans += csum
            group = False
            valid = False
            csum = 0

    return ans

@solution_timer(2023, 3, 2)
def part_two(inp):
    ans = 0
    gears = {}

    for y, line in enumerate(inp):
        csum = 0
        group = False
        lgear = []
        for x, char in enumerate(line):
            if char.isnumeric():
                if group:
                    csum = csum * 10 + int(char)
                else:
                    csum = int(char)
                    group = True

                # look for gear
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        if (0 <= x + i)and (x+i < len(line)) and (0 <= y + j) and (y + j < len(inp)):
                            if (inp[y + j][x + i] == '*'):
                                if (x+i, y+j) not in lgear:
                                    lgear.append((x+i, y+j))
            else:
                if group:
                    for gear in lgear:
                        if gear in gears:
                            gears[gear].append(csum)
                        else:
                            gears[gear] = [csum]
                    csum = 0
                    group = False
                    lgear = []
        if group:
            for gear in lgear:
                if gear in gears:
                    gears[gear].append(csum)
                else:
                    gears[gear] = [csum]
            group = False
            lgear = []

    for key, val in gears.items():
        if len(val) == 2:
            ans += val[0] * val[1]
        elif len(val) >= 3:
            print("eys")
    return ans

if __name__ == '__main__':
    inp = get_input(2023, 3)
    part_one(inp)
    part_two(inp)
