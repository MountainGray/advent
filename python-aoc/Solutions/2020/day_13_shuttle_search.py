file=open('Day13/input.txt')
lines=file.read().splitlines()
order=lines[1].split(',')
buses=[]
#sort

for i, val in enumerate(order):
    if val!='x':
        buses.append([int(val),int(i)])

index=1
delta=1
steps=[]
while True:
    for i, bus in enumerate(buses):
        if (index+bus[1])%bus[0]==0 and bus not in steps:
            steps.append(bus)
            delta*=bus[0]
        elif bus in steps:
            continue
        else:
            break
    if buses== steps:
        break
    else:
        index+=delta

print(index)