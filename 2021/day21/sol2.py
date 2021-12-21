inp = open('2021/day21/input.txt').read().split('\n')
import time 
start = time.time()
p1 = int(inp[0][-1:])
p2 = int(inp[1][-1:])
p1score  = 0
p2score  = 0

possrolls = []
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            possrolls.append(i+j+k)

optim = []
for i in range(3,10):
    optim.append([i, possrolls.count(i)])
    
def getwinner(p1,p2,p1score, p2score, turn, dieroll):
    if turn == 0:
        p1 += dieroll
        p1%=10
        p1score += p1 + 1
        if p1score >=21:
            return [1,0]
        else:
            outcome = [0,0]
            for roll, mu in optim:
                one, two = getwinner(p1,p2,p1score, p2score, 1, roll)
                outcome[0] += one * mu
                outcome[1] += two * mu
            return outcome
    else:
        p2 += dieroll
        if p2%10 == 0:
            p2score += 10
            p2 = 10
        else:
            p2score += p2%10
            p2 = p2%10
        if p2score >=21:
            return [0,1]
        else:
            outcome = [0,0]
            for roll, mu in optim:
                one, two = getwinner(p1,p2,p1score, p2score, 0, roll)
                outcome[0] += one * mu
                outcome[1] += two * mu
            return outcome


total = [0,0]
for roll, mul in optim:
    x, y = getwinner(p1,p2,p1score, p2score, 0, roll)
    total[0] += x * mul
    total[1] += y * mul
print(total)
print(time.time()-start)