inp = open('2021/day18/input.txt').read().split('\n')
import ast
from math import floor, ceil
b = []
for line in inp:
    b.append(ast.literal_eval(line))

class Node:
    
    def __init__(self, lis, depth) -> None:
        self.depth = depth
        if isinstance(lis[0],list):
            self.a = Node(lis[0],depth+1)
        else:
            self.a = lis[0]
        if isinstance(lis[1], list):
            self.b = Node(lis[1],depth+1)
        else:
            self.b = lis[1]
    
    def __repr__(self) -> str:
        return f"[{self.a},{self.b}]"

    def sumer(self):
        v1 = self.a if isinstance(self.a,int) else self.a.sumer()
        v2 = self.b if isinstance(self.b,int) else self.b.sumer()
        return v1*3 + v2*2

    def addright(self,val):
        if isinstance(self.a,Node):
            self.a.addright(val)
        else:
            self.a += val


    def addleft(self,val):
        if isinstance(self.b,Node):
            self.b.addleft(val)
        else:
            self.b += val
    def update_spl(self):
        if isinstance(self.a,int) and self.a>=10:
            self.a = Node([floor(self.a/2),ceil(self.a/2)],self.depth+1)
            return 1
        elif isinstance(self.a, Node):
            t = self.a.update_spl()
            if t==1:
                return 1
        if isinstance(self.b,int)and  self.b>=10:
            self.b = Node([floor(self.b/2),ceil(self.b/2)],self.depth+1)
            return 1
        elif isinstance(self.b, Node):
            t = self.b.update_spl()
            if t==1:
                return 1
        return 0

    def update(self):
        if self.depth >=4 and isinstance(self.a, int) and isinstance(self.b,int):
            #print("exp",end="")
            return 2, self.a, self.b
        if isinstance(self.a, Node):
            ret, a, b = self.a.update()
            if ret ==2:
                self.a = 0
            if ret != 0:
                if b:
                    if isinstance(self.b, Node):
                        self.b.addright(b)
                    else:
                        self.b += b
                return 1, a, None
        if isinstance(self.b, Node) :
            ret, a, b= self.b.update()
            if ret ==2:
                self.b = 0
            if ret != 0:
                if a:
                    if isinstance(self.a,Node):
                        self.a.addleft(a)
                    else:
                        self.a +=a
                return 1, None, b
        return 0, None, None
            

c = []
for x in b:
    ne = Node(x,0)
    c.append(ne)
#base = Node(b[0],0) 
#while True:
    #t,_,_ = base.update()
    #print(base)
    #if t==0:
        #q =base.update_spl()
        #if q==0:
            #break

comp = b[0]
for node in b[1:]:
    print(comp)
    print("+ ",node) 
    comp = Node([comp,node],0)
    old = str(comp)
    while True:
        t,_,_ = comp.update()
        if t==0:
            q =comp.update_spl()
            if q==0:
                break
    comp = ast.literal_eval(str(comp))
    print("=",comp)

comp = Node(comp, 0)
print(comp.sumer())

mx = 0
for i in range(len(b)):
    for j in range(len(b)):
        if i != j:
            comp = Node([b[i],b[j]],0)
            while True:
                t,_,_ = comp.update()
                if t==0:
                    q =comp.update_spl()
                    if q==0:
                        break
            mx = comp.sumer() if comp.sumer()>mx else mx

print(mx)
            
