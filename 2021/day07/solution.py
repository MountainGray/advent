inp = [int(x) for x in open('2021/day07/input.txt').read().split(',')]
from math import factorial

def solve():
    ans = find_fuel(inp, 0)
    for i in range(1, max(inp) + 1):
        temp = find_fuel(inp, i)
        ans = temp if temp < ans else ans
    return ans

def find_fuel(subs, idx)-> int:
    tot = 0
    for pos in subs:
        tot += sum(range(1,(abs(pos-idx)+1)))
    return tot
print(solve())
    

