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
for i in log:
    print(i)


#submit(2018,4,1,ans)