from collections import Counter
file=open("Day6/input.txt", "r")
lines=file.read().splitlines()

total=0
questionstring=[]
size_group=[]
group=""
numpersons=0
for line in lines:
    if line=="":
        questionstring.append(group)
        size_group.append(numpersons)
        group=""
        numpersons=0
    else:
        group+=line
        numpersons+=1

questionstring.append(group)
size_group.append(numpersons)
'''
Part1 solution, use set to kill repeats, then just find length of line 
pro_groups=[]
for line in groups:
    pro_groups.append("".join(set(line)))
print(pro_groups)

for i in pro_groups:
    total+=len(i)
'''
for i, string in enumerate(questionstring):
    counterd=Counter(string)
    for j in counterd:
        if counterd[j]==size_group[i]:
            total+=1
print(total)
#woowowoowow dub between amigos, not part one but part 2
#part1 6615
#part 2 3360
