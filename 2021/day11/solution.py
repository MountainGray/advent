inp = open('2021/day11/input.txt').read().split('\n')
squid = [[int(x)for x in line]for line in inp]
total = 0
p = 0
while True:
    for i in range(len(squid)):
        for j in range(len(squid[0])):
            squid[i][j] +=1
    changed = True
    while changed:
        changed = False
        for i in range(len(squid)):
                for j in range(len(squid[0])):
                    if squid[i][j] > 9:
                        squid[i][j] = 0
                        changed = True
                        total += 1
                        for k in range(-1,2):
                            for l in range(-1,2):
                                if i+k >= 0 and i+k < len(squid) and j+l >= 0 and j+l < len(squid[0]):
                                    if squid[i+k][j+l] != 0:
                                        squid[i+k][j+l] +=1
    p += 1
    if p == 100:
        print("P1:",total)
    sync = True
    for i in range(len(squid)):
        for j in range(len(squid[0])):
            if squid[i][j] != 0:
                sync = False
    if sync:
        print("P2:",p)
        break
    


