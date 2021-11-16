file=open('Day10/input.txt','r')
lines=file.read().splitlines()
adapters=[int(x)for x in lines]
adapters.append(0)
adapters.sort()
max=adapters[-1]
ones=0
threes=0
for i in range(1,len(adapters)):
    if adapters[i]-adapters[i-1]==1:
        ones+=1
    if adapters[i]-adapters[i-1]==3:
        threes+=1
memo={len(adapters)-1:1}
for i in range(len(adapters)-2,-1,-1):
    paths_ahead=0
    j=1
    while i+j <len(adapters) and j<4:
        if adapters[i+j]-adapters[i]<=3:
            paths_ahead+=memo[i+j]
        j+=1
    memo[i]=paths_ahead

print(memo[0])
    

# we dont talk about the code below


class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = []
    def getkids(self):
        return self.children
    def addkid(self, obj):
        self.children.append(obj)
    def findposs(self):
        total=0
        if self.children==[]:
            total+=1
        else:
            for child in self.children:
                total+=child.findposs()
        return total
    def __str__(self) -> str:
        out=str(self.value)+" ("
        for child in self.children:
            out+=str(child)+" "
        out+=')'
        return out
    def __repr__(self) -> str:
        return self.value
def find_nodes_forward(root, list, i):
    if i==len(list)-1:
        return
    j=3 if i+3<len(list)else len(list)-i-1
    val=[]
    for k in range(i+1,i+j+1):
        if list[k]-list[i]<=3:
            val.append(k)
    if len(val)>1:
        for l in val:
            newnode=Node(list[l])
            root.addkid(newnode)
            findNodes(newnode,list,l)
    else:
        findNodes(root,list,i+1)
