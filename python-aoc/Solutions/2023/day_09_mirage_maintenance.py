from advent import get_input, solution_timer, submit


@solution_timer(2023, 9, 1)
def part_one(inp):

    ans = 0
    for line in inp:
        tl = list(map(int,line.split()))
        hist = [tl]
        while True:
            ntl = []
            for i in range(len(tl)-1):
                ntl.append(tl[i+1]- tl[i])
            hist.append(ntl)
            tl = ntl
            if all([x == 0 for x in ntl]):
                break
        
        cval = 0
        tsum = 0
        for i in reversed(range(len(hist))):
            cval = hist[i][-1] + cval
            print(cval)
            tsum += cval
        print(tsum)
        ans += cval 
            
    return ans



@solution_timer(2023, 9, 2)
def part_two(inp):
    ans = 0
    for line in inp:
        tl = list(map(int,line.split()))
        hist = [tl]
        while True:
            ntl = []
            for i in range(len(tl)-1):
                ntl.append(tl[i+1]- tl[i])
            hist.append(ntl)
            tl = ntl
            if all([x == 0 for x in ntl]):
                break
        
        cval = 0
        tsum = 0
        for i in reversed(range(len(hist))):
            cval = hist[i][0] - cval
            tsum += cval
        ans += cval 
            
    return ans


if __name__ == "__main__":
    #test = get_input(2023, 9, filename="test.txt")
    test= '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''.splitlines()
    #print("Test:")
    part_one(test)
    inp = get_input(2023, 9)
    ans = part_one(inp)
    #submit(2023, 9, 1, ans)
    #part_two(test)
    ans = part_two(inp)
    submit(2023, 9, 2, ans)

