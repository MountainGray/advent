inp = [int(x) for x in open('2020/day01/input.txt').read().split('\n')]

#p1
for i in inp:
    for j in inp:
            if i+j==2020:
                print("P1",i*j)

#p2
for i in inp:
    for j in inp:
        for k in inp:
            if i+j+k==2020:
                print("P2:",i * j * k)