inp = open('2021/day21/input.txt').read().split('\n')
p1 = int(inp[0][-1:])
p2 = int(inp[1][-1:])
dieroll = 0

p1score  = 0
p2score  = 0

die = 1
rolls = [i for i in range(3)]

#while True:
    #sumdi = 0
    #for i in range(3):
        #sumdi += die
        #die +=1
        #if die == 101:
            #die = 1
    #dieroll +=3
    #p1 += sumdi
    #if p1%10 == 0:
        #p1score += 10
        #p1 = 10
    #else:
        #p1score += p1%10
        #p1 = p1%10
    #if p1score >=1000:
        #print(p2score*dieroll)
        #break
    
    #sumdi = 0
    #for i in range(3):
        #sumdi += die
        #die +=1
        #if die == 101:
            #die = 1
    #dieroll +=3
    #p2 += sumdi
    #if p2%10 == 0:
        #p2score += 10
        #p2 = 10
    #else:
        #p2score += p2%10
        #p2 = p2%10
    #if p2score >=1000:
        #print(p1score*dieroll)
        #break

possrolls = []
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            possrolls.append(i+j+k)


def getwinner(p1,p2,p1score, p2score, turn, dieroll):
    sumdi = 0
    if turn == 0:
        p1 += dieroll
        if p1%10 == 0:
            p1score += 10
            p1 = 10
        else:
            p1score += p1%10
            p1 = p1%10
        if p1score >=21:
            return [1,0]
        else:
            outcome = [0,0]
            for i in possrolls:
                one, two = getwinner(p1,p2,p1score, p2score, 1, i)
                outcome[0] += one
                outcome[1] += two
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
            for i in possrolls:
                one, two = getwinner(p1,p2,p1score, p2score, 0, i)
                outcome[0] += one
                outcome[1] += two
            return outcome

total = []
for i in possrolls:
    x, y = getwinner(p1,p2,p1score, p2score, 0, i)
    total[0] += x
    total[1] += y
print(total)