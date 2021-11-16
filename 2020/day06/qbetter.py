
from collections import Counter
file=open("Day6/input.txt", "r")
groups=file.read().split("\n\n")

total=0
groupstrings=[]
size_group=[]
personstring=""
numpersons=0
for group in groups:
    people=group.splitlines()
    st=""
    size_group.append(len(people))
    for person in people:
        st+=person
    groupstrings.append(st)

'''
Part1 solution, use set to kill repeats, then just find length of line 
pro_groups=[]
for line in groups:
    pro_groups.append("".join(set(line)))
print(pro_groups)

for i in pro_groups:
    total+=len(i)
'''
for i, string in enumerate(groupstrings):
    counter=Counter(string)
    print(counter)
    for j in counter:
        if counter[j]==size_group[i]:
            total+=1
print(total)
#woowowoowow dub between amigos, not part one but part 2
#part1 6615
#part 2 3360
