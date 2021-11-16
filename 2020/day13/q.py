file=open('Day13/input.txt')
lines=file.read().splitlines()

note=int(lines[0])
BusList = lines[1]
Sol1=set(BusList.split(','))
print(Sol1)
Sol1.remove('x')
Sol2=BusList.split(',')

val={}
for i,bus in enumerate(Sol2):
    val[bus]=i
val.pop('x')
print(val)


i=note
bustaken=0
found=False
while True:
    for j in Sol1:
        if i%int(j)==0:
            bustaken=int(j)
            found=True
            break 
    if found==True:
        break
    i+=1
x=(i-note)*bustaken
print(x)

'''
combonation increasing
constantly look ahead at the next computable match
find first match, bf till second then increment by the # till repeat
'''

easy=val.keys()
print(easy)

start=100000000000000
passes=False
distance=easy[0][0]
print(distance)
while True:
    index=0
    if passes==True:
        break
    else:
        break

    #for key, value in val.items():

        
    

'''
while True:
    if chart[i%len(chart)]!='x':
        print(chart[i%len(chart)])
        bustaken=int(chart[i%len(chart)])
        break
    else:
        i+=1
'''