f='Day25/input.txt'
fl=open(f)
lines=fl.read().splitlines()
print(lines)
rem=20201227
# operation
# start at val = 1
# val = val * x
#  val = val % rem
# sn is shared
val = 1
sn=7
ls=8
for i in range(ls):
    val = val * sn % rem
print(val)
sn=7
v1=0
v2=0
val=1
times=1
while True:
    val = val * sn % rem
    if val==int(lines[0]):
        v1=times
    elif val==int(lines[1]):
        v2=times
    if v1!=0 and v2!=0:
        break
    else:
        times+=1

print(v1)
print(v2)
print(sn)
val=1
sn=int(lines[0])
for i in range(v2):
    val = (val * sn) % rem
print(val)

    
