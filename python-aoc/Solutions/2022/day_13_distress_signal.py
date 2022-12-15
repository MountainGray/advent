from advent import get_input, submit
from functools import cmp_to_key
inp = get_input(2022, 13, split_char="\n\n")

def compare(a,b):
    match a, b:
        case list(a), list(b):
            for i in range(len(a)):
                if i >= len(b):
                    return -1
                elif compare(a[i], b[i])== -1:
                    return -1
                elif compare(a[i], b[i])== 1:
                    return 1
            if len(b) > len(a):
                return 1
            return 0
        case list(a), int(b):
            return compare(a, [b])
        case int(a), list(b):
            return compare([a], b)
        case _, _:
            if a <b:
                return 1
            elif a == b:
                return 0
            else:
                return -1

ans = 0
for idx, i in enumerate(inp):
    a,b = list(map(eval, i.split("\n")))
    if compare(a,b)!=-1:
        ans += idx+1

print(ans)


inp = get_input(2022, 13, split_char="\n")

inp = list(filter(lambda x: x != "", inp))
inp = list(map(eval, inp))
inp.append([[2]])
inp.append([[6]])
changed = True
while changed==True:
    changed = False
    for i in range(len(inp)-1):
        if compare(inp[i], inp[i+1])==-1:
            inp[i], inp[i+1] = inp[i+1], inp[i]
            changed = True

ans = (inp.index([[2]])+1) *( inp.index([[6]])+1)
print(ans)
if __name__ == '__main__':

    pass
    #submit
