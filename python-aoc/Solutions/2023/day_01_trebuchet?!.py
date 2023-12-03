from advent import get_input

inp = get_input(2023, 1)

nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five" : 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

ans = 0
number = []
for line in inp:
    i = 0
    n = []
    while i < len(line):
        if line[i].isnumeric():
            n += [int(line[i])]

        for k, v in nums.items():
            if i + len(k) - 1 < len(line) and line[i:i+len(k)] == k:
                n += [v]
                break
        i+=1
    number.append(n)

ans = sum(map(lambda x: x[0]*10 + x[-1], number))
print(ans)

