inp = open("2020/day02/input.txt").read().split("\n")

# p1
valid = 0
for line in inp:
    num, letter, seq = line.split(" ")
    low, high = [int(x) for x in num.split("-")]
    if low <= seq.count(letter[0]) <= high:
        valid += 1

print("P1:", valid)

# p2
valid = 0
for line in inp:
    num, letter, seq = line.split(" ")
    low, high = [int(x) for x in num.split("-")]
    if (letter[0] == seq[low-1]) ^ (letter[0] == seq[high-1]):
        valid +=1
print("P2:",valid)
#:(
