start,inp = open('2021/day14/input.txt').read().split('\n\n')
start = start
print(start)

paris = {}

for line in inp.split("\n"):
    pair, ins = line.split(" -> ")
    paris[pair] = ins

current = {}

for i in range(len(start)-1):
    if start[i:i+2] not in current:
        current[start[i:i+2]] = 1
    else:
        current[start[i:i+2]] += 1


print(current)
bias = {}
for i in start:
    if i not in bias:
        bias[i] = 1
    else:
        bias[i] += 1

print(bias)
for _ in range(40):

    new = {}
    for key, value in current.items():
        ins = paris[key]
        if ins not in bias:
            bias[ins] =  value
        else:
            bias[ins]+=value
        
        if key[0]+ins not in new:
            new[key[0]+ins] = value
        else:
            new[key[0]+ins] += value

        if ins+key[1] not in new:
            new[ins+key[1]] = value
        else:
            new[ins+key[1]] += value

    current = new



    # for i in range(len(start)-1):
    #     if start[i:i+2] in paris:
    #         new.append(start[i]+paris[start[i:i+2]])
    #     else:
    #         new.append(start[i])
    # new.append(start[-1])

    #start = "".join(new)

# count = {}
# for key, value in current.items():
#     if key[0] not in count:
#         count[key[0]] = value
#     else:
#         count[key[0]] += value

#     if key[1] not in count:
#         count[key[1]] = value
#     else:
#         count[key[1]] += value



x = [i for i in bias.values()]

x.sort()
print(x)
print(x[-1]-x[0])
