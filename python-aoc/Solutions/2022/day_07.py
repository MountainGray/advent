from advent import get_input, solution_timer
inp = get_input(2022, 7)

cd = ["/"]
fs ={}

for i in inp:
    b = i.split()

    if b[0] == "$":
        if b[1] == "cd":
            if b[2] == "..":
                cd = cd[:-1]
            elif b[2]== "/":
                cd = ["/"]
            else:
                cd = cd +[b[2]]
                print(cd, "added")
        elif b[1] == "ls":
            continue
    else:
        dr = "".join(cd)
        if dr not in fs:
            fs[dr] = []
        
        fs["".join(cd)] += [b]

tot = {}
def sumfs(dr: str):
    lis = fs[dr]
    s = 0
    for i in lis:
        if i[0] == "dir":
            print(dr, i)
            s += sumfs(dr+i[1])
        else:
            s += int(i[0])
    return s
for i in fs.keys():
    tot[i] = sumfs(i)

ans = 0
for b, val in tot.items():
    if val <= 100000:
        print(b, val)
        ans += val

mas = 70000000
mas -= tot["/"]

l = list(tot.values())
l.sort()
for i in l:
    if mas + i >= 30000000:
        ans = i
        break

print(ans)
