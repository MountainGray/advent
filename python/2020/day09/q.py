file=open("Day9/input.txt","r")
lines=file.read().splitlines()
answer1=0
past25=[]

for i in range(25):
    past25.append(int(lines[i]))
for i in range(25, len(lines)):
    passes=False
    for j in past25:
        for k in past25:
            if int(j)+int(k)==int(lines[i]) and int(j) != int(k):
                passes=True
    if passes==False:
        answer1=int(lines[i])
        break
    past25.pop(0)
    past25.append(lines[i])

print(answer1)
Minimum=0
Maximum=0
for i in range(len(lines)):
    acc=int(lines[i])
    min=int(lines[i])
    max=int(lines[i])
    for j in range(i+1,len(lines)):
        acc=acc+int(lines[j])
        if int(lines[j])>max:
            max=int(lines[j])
        elif int(lines[j])<min:
            min=int(lines[j])
        if acc>= answer1:
            break
    if acc==answer1:
        Minimum=min
        Maximum=max
        break

answer2=Maximum+Minimum
print(answer2)