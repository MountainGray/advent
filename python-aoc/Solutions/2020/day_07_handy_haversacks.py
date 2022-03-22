from collections import Counter
file=open("Day7/input.txt","r")
answer=0
#lines=file.read().split('\n\n')
lines=file.read().splitlines()
contains={}
times=0
'''
part 1
while True:
    temp=answer
    for line in lines:
        sec=line.split("contain")
        if sec[0][:-1] in contains:
            continue
        else:
            if "shiny gold" in sec[1]:
                contains[sec[0][:-2]]=1
            else:
                newcontains=contains.copy()
                for bag in newcontains.keys():
                    if bag in sec[1]:
                        contains[sec[0][:-2]]=1
    answer=len(contains)
    times+=1
    if times==answer:
        break
'''
allbags={}
for line in lines:
    kev= line.split("contain")
    outer=kev[0]
    outer=outer.replace(" bags ","")
    if kev[1]==" no other bags.":
        allbags[outer]={}
        continue
    bags=kev[1].split(",")
    bags[-1]=bags[-1][:-1]
    cancontain={}
    for bag in bags:
        val=bag[1]
        typ= bag[3:]
        typ=typ.replace(" bags","")
        typ=typ.replace(" bag","")
        cancontain[typ]=val
    if outer in allbags:
        continue
    else:
        allbags[outer]=cancontain


def recurse(key):
    if allbags[key]=={}:
        return 1
    else:
        total_bags=1
        for i, val in allbags[key].items():
            total_bags+=int(val)*recurse(i)
        return total_bags
ans=recurse("shiny gold")
print(ans)
