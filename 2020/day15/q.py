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
