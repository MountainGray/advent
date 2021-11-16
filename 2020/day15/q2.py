file=open('Day15/input.txt')
lines=file.read().split(',')
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
