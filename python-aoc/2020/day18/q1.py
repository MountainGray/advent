file = open('Day18/input2.txt')
lines=file.read().splitlines()
total=0

expressions=[]
for line in lines:
    expressions.append(''.join([i for i in line if i!=' ']))

def parse(expr):
    def _helper(iter):
        items = []
        for item in iter:
            if item == '(':
                result, closeparen = _helper(iter)
                if not closeparen:
                    raise ValueError("bad expression -- unbalanced parentheses")
                items.append(result)
            elif item == ')':
                return items, True
            else:
                items.append(item)
        return items, False
    return _helper(iter(expr))[0]   

lists=[]
for line in expressions:
    lists.append(parse(line))

print(lists)

def solve(ex):
    tot=0
    op='+'
    i=0
    for i in ex:
        if isinstance(i, list):
            if op=='+':
                tot+=solve(i)
            elif op=='*':
                tot*=solve(i)
        elif i=='+':
            op='+'
        elif i=='*':
            op='*'
        else:
            if op=='+':
                tot+=int(i)
            else:
                tot*=int(i)
    return tot

for i in lists:
    total+=solve(i)
print(total)

         
'''
    def solve(expr):
        total=0
        for i, char in enumerate(expr):
            if char =='(':
                depth=1
                span=0
                for j,char2 in enumerate(expr[i+1:]):
                    if char2=='(':
                        depth+=1
                    elif char2==')':
                        depth-=1

                    if depth==0:
                        span=j
                        break
                
                solve(expr[i+1:i+j])
            if char=='+'
            else:
'''




                