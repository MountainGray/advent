inp = open('2021/day20/input.txt').read().split('\n\n')
enhancement, inp = inp
enhancement = enhancement.replace('\n', '')
inp = inp.split('\n')


def paddot(list):
    new = []
    new.append("."*(len(list[0])+10))
    new.append("."*(len(list[0])+10))
    new.append("."*(len(list[0])+10))
    new.append("."*(len(list[0])+10))
    new.append("."*(len(list[0])+10))
    for i in list:
        new.append("....."+i+".....")
    new.append("."*(len(list[0])+10))
    new.append("."*(len(list[0])+10))
    new.append("."*(len(list[0])+10))
    new.append("."*(len(list[0])+10))
    new.append("."*(len(list[0])+10))
    return new

def padhash(list):
    new = []
    new.append("#"*(len(list[0])+10))
    new.append("#"*(len(list[0])+10))
    new.append("#"*(len(list[0])+10))
    new.append("#"*(len(list[0])+10))
    new.append("#"*(len(list[0])+10))
    for i in list:
        new.append("#####"+i+"#####")
    new.append("#"*(len(list[0])+10))
    new.append("#"*(len(list[0])+10))
    new.append("#"*(len(list[0])+10))
    new.append("#"*(len(list[0])+10))
    new.append("#"*(len(list[0])+10))
    return new


def strip(list):
    new = []
    for i in list[4:-4]:
        new.append(i[4:-4])
    return new
for i in range(50):
    if i%2 == 0:
        inp = paddot(inp)
    else:
        inp = padhash(inp)
    #inp = paddot(inp)
    new = []
    for i in range(1,len(inp[0])-1):
        for j in range(1,len(inp)-1):
            bstr = inp[j-1][i-1:i+2] + inp[j][i-1:i+2] + inp[j+1][i-1:i+2]
            bstr = bstr.replace("#","1").replace(".","0")
            bstr = int("0"+bstr,2)
            new.append([i,j,enhancement[bstr]])


    
    for i,j,nc in new:
        inp[j] = inp[j][:i]+nc+inp[j][i+1:]
    #for i in inp:
        #print(i)
    #print()
    inp = strip(inp)

total = 0
for i in inp:
    for char in i:
        if char == "#":
            total += 1

print(total)



