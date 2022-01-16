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
print(run)
mask=[]
memory={}
for instruct in run:
    if instruct[0]=='mask':
        mask=[]
        for mchar in instruct[1]:
            mask.append(mchar)
    else:
        val=''
        bin='{0:b}'.format(instruct[1])
        for i, op in enumerate(mask):
            if len(mask)-i>len(bin):
                val+=op
            else:
                if op=='1' or op=='0':
                        val+=mask[i]
                else:
                    val+=bin[i-(len(mask)-len(bin))]
        memory[instruct[0]]=val
total=0
for i, val in memory.items():
    total+=int(val,2)
print(total)

            




