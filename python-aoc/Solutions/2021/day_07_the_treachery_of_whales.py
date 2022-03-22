inp = [int(x) for x in open('2021/day07/input.txt').read().split(',')]
print("P1:", min(map(lambda y: sum(map(lambda x: abs(x-y), inp)),range(max(inp)+1))))
print("P2:", min(map(lambda y: sum(map(lambda x: abs(x-y)*(abs(x-y)+1)//2, inp)), range(max(inp)+1))))