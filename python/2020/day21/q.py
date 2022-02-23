fr=open('Day21/input.txt')
ip=fr.read().splitlines()
options={}
for line in ip:
    ingredients, alergens=line.split(' (contains ')
    alergens=alergens[:-1].split(', ')
    ingredients=ingredients.split()
    for alergy in alergens:
        if alergy not in options:
            options[alergy]=set(ingredients)
        else:
            nset=options[alergy].copy()
            for ing in options[alergy]:
                if ing not in ingredients:
                    nset.remove(ing)
            options[alergy]=nset
while True:
    leave=True
    for key, val in options.items():
        if len(val)==1:
            for key2,val2 in options.items():
                if key!=key2 :
                    options[key2]=val2-val
        else:
            leave=False
    if leave==True:
        break
alergens=set()
for val in options.values():
    alergens=alergens.union(val)
ans1=0
for line in ip:
    ingredients=line.split(' (contains ')[0].split()
    for ing in ingredients:
        if ing not in alergens:
            ans1+=1
print(ans1)
ans2=''
ordop=sorted(options)
for i in ordop:
    ans2+=str(options[i])[2:-2]+','
print(ans2[:-1])    