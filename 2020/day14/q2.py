import random
file = open('Day14/input.txt')
lines=file.read().splitlines()
run=[]
for i, line in enumerate(lines):
    split=line.split(' = ')
    if split[0]=='mask':
        run.append(split)
    else:
        num=int(split[0][4:-1])
        val=int(split[1])
        run.append([num,val])


mask=[]
memory={}
for instruct in run:
    if instruct[0]=='mask':
        mask=[]
        for mchar in instruct[1]:
            mask.append(mchar)
    else:
        val=''
        bin='{0:b}'.format(instruct[0])
        for i, op in enumerate(mask):
            if len(mask)-i>len(bin):
                val+=op
            else:
                if op=='1' or op=='X':
                        val+=mask[i]
                else:
                    val+=bin[i-(len(mask)-len(bin))]
        memory[instruct[1]]=val

ram={}
for value ,address in memory.items():
    times=2**address.count("X")
    tried=[]
    for i in range(times):
        mod=[i for i in address]
        while True:
            for i, ch in enumerate(address):
                if ch=='X':
                    mod[i]=str(random.randint(0,1))
            tester=''.join(mod)
            if tester not in tried:
                tried.append(tester)
                ram[int(tester,2)]=value
                break

total=0
for i, val in ram.items():
    total+=val
print(total)



            




