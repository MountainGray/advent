inp = open('2015/day05/input.txt').read().split('\n')[:]
import re
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
gs=0
for line in inp:
    qual = 0
    char = set(line)
    for ch in char:
        regex= re.compile(f"{ch}.{ch}")
        if regex.search(line):
            qual+=1
            break
    
    done= False
    for ch in char:
        for ch2 in char:
            regex = re.compile(f"{ch}{ch2}")
            if len(regex.split(line))>2:
                print(regex.split(line))
                qual+=1
                done=True
                break
        if done:
            break

    if qual >=2:
        gs+=1

print("P2:", gs)

    