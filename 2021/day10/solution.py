inp = open('2021/day10/input.txt').read().split('\n')
corrupted = [
    '(]', '{()()()>', '(((()))}', '<([]){()}[{}])'
]
score = {
    ')': 1,
']': 2,
'}': 3,
'>': 4
}
score2 = {
    '(': 1,
'[': 2,
'{': 3,
'<': 4
}

match = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}
start = ['<', '{', '[', '(']
end = ['>', '}', ']', ')']
total = 0
total1 = []
for line in inp:
    stack = []
    corrupted = False
    for symbol in line:
        if symbol in start:
           stack.append(symbol)
        elif symbol in end:
            if len(stack) == 0:
                total += score[symbol]
                corrupted = True
                break
            elif match[symbol] != stack[-1]:
                total += score[symbol]
                corrupted = True
                break
            else:
                stack.pop()
    if not corrupted:
        linetot = 0
        stack.reverse()
        for symbol in stack:
            linetot = linetot*5 +score2[symbol]

        total1.append(linetot)

    
total1.sort()
print(total1)

print(total)
print(total1[len(total1)//2 ])

