from advent import get_input, submit
inp = get_input(2018, 4)
ans = 0

log = []
for i in inp:
    ymd, time, *text = i.split()
    year, month, day = ymd[1:].split("-")
    hour, minute = time[:-1].split(":")
    vals = (year, month, day, hour, minute, text)
    log.append(vals)
log.sort()

guards = {}
guard = 0
start = 0
for i in log:
    *date, text = i
    if text[0] == "Guard":
        num = int(text[1][1:])
        guard = num
        if num not in guards:
            guards[num] = [0 for i in range(60)]
    elif text[0] == "falls":
        *t, minute = date
        start = int(minute)
    else:
        *t, minute = date
        minute = int(minute)
        record = guards[guard]
        for i in range(start, minute+1):
            record[i] += 1
        guards[guard] = record

leader = guards.items()
print(leader)
leader = [(i, sum(x)) for i, x in leader]
leader.sort(key=lambda t: (t[1]))
w = leader[0][0]
b = guards[w].index(max(guards[0][1]))
ans = w * b
print(ans)



#submit(2018,4,1,ans)