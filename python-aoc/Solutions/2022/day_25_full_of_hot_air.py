from advent import get_input
inp = get_input(2022, 25)
val = {
    "2" :2,
    "1" :1,
    '0' :0,
    '-' : -1,
    '=' : -2,
}
trans = ["=", '-', '0', '1', '2']
ss = 0
def get_val(char_list):
    s=0
    for idx, char in enumerate(reversed(char_list)):
        s += val[char] * (5**idx)
    return s


for line in inp:
    ss += get_val(line)
print(ss)
i=0

def sum_nums(vals):
    s=0
    for idx, i in enumerate(reversed(vals)):
        s += i * (5**idx)
    return s
#x=sum_nums([-2, -2, 0, 0, 1, -2, -1, 2, -2, -1, -1, 0, 2, 1, 2, -1, 2, 2, -1, 2])
#assert x == ss
#exit()

vals = [0 for _ in range(20)]
vals[0]=2

cs = sum_nums(vals)
print(cs)

while True:
    for idx in range(20):
        for i in range(5):
            v2 = vals.copy()
            v2[idx] = i-2 
            print(vals)
            print(v2)
            c2=sum_nums(v2)

            if c2 == ss:
                print("found", cs,ss)
                print(v2)
                print("".join([trans[i+2] for i in v2]))
                exit()
            elif abs(c2-ss) < abs(cs-ss):
                cs = c2
                vals = v2
                print("new best", cs, abs(cs-ss))
