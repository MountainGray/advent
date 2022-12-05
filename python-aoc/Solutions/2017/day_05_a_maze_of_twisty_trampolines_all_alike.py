from advent import get_input, submit
inp = get_input(2017, 5)
ans = 0
inp = [int(i) for i in inp]
x = 0
while True:
    if x >= len(inp):
        break
    else:
        xn = x+inp[x]
        inp[x] += 1 if inp[x] < 3 else -1
        x = xn
        ans += 1

# CHANGE FOR PART 2!!
submit(2017, 5, 2, ans)