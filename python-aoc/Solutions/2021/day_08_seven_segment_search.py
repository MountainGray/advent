from itertools import permutations
inp = open('2021/day08/input.txt').read().split('\n')
sequences = [line.replace("| ", "").split(" ") for line in inp]
#p1
tot = sum(map(lambda x:1 if len(x) == 2 or len(x) ==  7 or len(x)== 4 or len(x) == 3 else 0 ,[seq for sequence in sequences for seq in sequence[-4:]]))
print("P1:", tot)

lets = ["a", "b", "c", "d", "e", "f", "g"]
perms = permutations(lets)
permdicts = [{v:k for k,v in zip(lets, perm)}for perm in perms]
gltr= {"abcdefg": 8, "abdfg": 5, "acdeg": 2, "acdfg": 3, "acf": 7, "abcdfg": 9, "abdefg": 6, "bcdf": 4, "abcefg": 0, "cf": 1}

def convert(translation, word):
    return ''.join(sorted([translation[char] for char in word]))

tot = 0
for i in range(len(sequences)):
    for translation in permdicts:
        if any(map(lambda x:convert(translation, x) not in gltr.keys(), sequences[i])):
            continue
        else:
            tot += sum([gltr[convert(translation,sequences[i][-1-x])] * val for x, val in enumerate([1, 10, 100 ,1000])])
            break
print("P2",tot)
    