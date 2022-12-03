from advent import get_input, solution_timer

@solution_timer(2017, 3, 1)
def part_1(inp):
    ans = 0
    x = 0
    y = 0

    for i in range(1, inp):
        if abs(x) == abs(y) and y>0 and x>0: x -= 1
        elif abs(x)== abs(y) and y<=0 and x<=0: x += 1
        elif abs(x) == abs(y) and y>0 and x<0: y -= 1
        elif abs(x) == abs(y) and y<0 and x>0: x += 1
        elif abs(x) > abs(y) and x >0: y += 1
        elif abs(x) > abs(y) and x<0: y -= 1
        elif abs(x) > abs(y) and x>0: y += 1
        elif abs(y) > abs(x) and y >0: x -= 1
        elif abs(y) > abs(x) and y <0: x += 1
    ans = abs(x) + abs(y)
    return ans

def translate(x, offset):
    return offset//2 + 1 + x

# I am not making the grid big enough theoretically, since I don't know how big it needs to be
# but we will terminate way before we hit that point
@solution_timer(2017, 3, 2)
def part_2(inp, ans_1=0):
    a = [[0 for i in range(ans_1+2)] for _ in range(ans_1+2)]
    ans = 0
    x = 0
    y = 0
    a[translate(x, ans_1)][translate(y, ans_1)] = 1
    for i in range(1, inp):
        if abs(x) == abs(y) and y>0 and x>0: x -= 1
        elif abs(x)== abs(y) and y<=0 and x<=0: x += 1
        elif abs(x) == abs(y) and y>0 and x<0: y -= 1
        elif abs(x) == abs(y) and y<0 and x>0: x += 1
        elif abs(x) > abs(y) and x >0: y += 1
        elif abs(x) > abs(y) and x<0: y -= 1
        elif abs(x) > abs(y) and x>0: y += 1
        elif abs(y) > abs(x) and y >0: x -= 1
        elif abs(y) > abs(x) and y <0: x += 1
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                a[translate(x, ans_1)][translate(y, ans_1)] += a[translate(x+i, ans_1)][translate(y+j, ans_1)]
        if a[translate(x, ans_1)][translate(y, ans_1)] > inp:
            ans = a[translate(x, ans_1)][translate(y, ans_1)]
            break
    return ans

if __name__ == '__main__':
    input = int(get_input(2017, 3)[0])
    x= part_1(input)
    part_2(input, x)