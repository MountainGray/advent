inp = open("2021/day03/input.txt", "r").read().split("\n")

def find_common(strs, idx, bias, flip):
    x,y = 0,0
    for i in strs:
        if i[idx] == "1":
            x+=1 * flip
        else:
            y+=1 * flip
    if x > y:
        return "1"
    elif y>x:
        return "0"
    else:
        return bias
gamma = "".join([find_common(inp,i,"1",1) for i in range(len(inp[0]))])
epsilon = "".join(['1' if i == '0' else '0' for i in gamma])
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print("P1",gamma*epsilon)

def find_bit(strs, bias, flip):
    solved = False
    while not solved:
        for i in range(len(strs[0])):
            x = find_common(strs, i, bias, flip)
            strs = list(filter(lambda z: z[i] == x, strs))
            if len(strs) == 1:
                solved = True
                break
    return strs[0]

oxygen_bits = inp.copy()
co2_bits = inp.copy()

oxygen_generator_rating = int(find_bit(oxygen_bits,"1", 1), 2)
co2_scrubber_rating= int(find_bit(co2_bits,"0", -1), 2)
print("P2:",oxygen_generator_rating*co2_scrubber_rating)