inp = open("2021/day03/input.txt", "r").read().split("\n")


def find_common(strs, idx, bias):
    x, y = 0, 0
    for i in strs:
        if i[idx] == bias:
            x += 1
        else:
            y += 1
    if x > y:
        return "1"
    elif y > x:
        return "0"
    else:
        return bias


gamma = "".join([find_common(inp, i, "1") for i in range(len(inp[0]))])
epsilon = "".join(["1" if i == "0" else "0" for i in gamma])
print(gamma)
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma,epsilon)
print("P1", gamma * epsilon)


def find_bit(strs, bias):
    for i in range(len(strs[0])):
        x = find_common(strs, i, bias)
        strs = list(filter(lambda z: z[i] == x, strs))
        print(len(strs))
        if len(strs) == 1:
            return strs[0]


oxygen_bits = inp.copy()
co2_bits = inp.copy()

oxygen_generator_rating = int(find_bit(oxygen_bits, "1"), 2)
co2_scrubber_rating = int(find_bit(co2_bits, "0"), 2)
print("P2:", oxygen_generator_rating * co2_scrubber_rating)
