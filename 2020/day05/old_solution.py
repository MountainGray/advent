text=open("Day5/input.txt","r")
lines=text.read().splitlines()
input_binary=[]
rows=[]
seats=[]
for line in lines:
    val=""
    for i in line:
        past=val
        if i =="B" or i =="R":
            val=past+"1"
        elif i=="F" or i=="L":
            val=past+"0"
    input_binary.append(val)
for i in range(len(input_binary)):
    row=input_binary[i][:7]
    columns=input_binary[i][7:]
    row=int(row , 2)
    rows.append(row)
    seat=int(columns, 2)
    seats.append(seat)
max=0
ids=[]
for i in range(len(rows)):
    ids.append( rows[i]*8+seats[i])
ids.sort()
for i in range(70, 826):
    if ids.count(i)==0:
        print(i)
