file = open('Day18/input2.txt')
lines=file.read().splitlines()
total=0


expressions=[]
for line in lines:
    expressions.append(''.join([i for i in line if i!=' ']))
#ooo an iterator method
def parse(expr):
    def _helper(iter):
        items = []
        for item in iter:
            if item == '(':
                result, closeparen = _helper(iter)
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
def presolve(ex):
    total=0
    sections=[]
    temp=[]
    
    for i,val in enumerate(ex):
        if isinstance(val ,list):
            temp.append(presolve(val))
        elif val=='*':
            sections.append(temp)
            sections.append('*')
            temp=[]
        else:
            temp.append(val)
    sections.append(temp)
    return sections

def solve(ex):
    tot=0
    #mults=[i for i, val in enumerate(expr) if val=='*']
    op='+'
    
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
    fixed=presolve(i)
    total+=solve(fixed)
print(total)
