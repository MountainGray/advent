inp = open('2015/day05/input.txt').read().split('\n')[:]

# Part 1
gs = 0
for line in inp:
    qual=0
    s = set(line)
    vowels = ['a', 'e', 'i', 'o', 'u']
    vc = 0
    for v in vowels:
        vc += line.count(v)
    if vc >= 3:
        qual += 1
    bad = ["ab", "cd", "pq", "xy"]
    for b in bad:
        if line.count(b) >= 1:
            qual -= 1
            break
    for x in s:
        if line.count(x+x) >= 1:
            qual += 1
            break
    if qual == 2:
        gs += 1

print("P1:", gs)
# Part 2
