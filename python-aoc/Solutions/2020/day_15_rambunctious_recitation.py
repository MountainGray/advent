file=open('Day15/input.txt')
lines=file.read().split(',')
said=[]

for i in lines:
    said.append(int(i))
print(lines)

for i in range(len(lines),2020):
    last=said[-1]
    if said.count(last)==1:
        said.append(0)
    else:
        indecies=[i for i, val in enumerate(said) if val==last]
        num=indecies[-1]-indecies[-2]
        said.append(num)
        
print(said[-1])

pastocur={}

for i, num in enumerate(lines[:-1]):
    pastocur[int(num)]=i
last=int(lines[-1])
for i in range(len(lines)-1,29999999):
    if last in pastocur:
        templast=last
        last=i-pastocur[last]
        pastocur[templast]=i
    else:
        pastocur[last]=i
        last=0
print(last)