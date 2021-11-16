fl=open('Day20/input.txt')
blocks=fl.read().split('\n\n')
blk=[]
for i in blocks:
    blk.append(i.splitlines())
print(blk)
print(len(blk))


class picture(object):
    def __init__(self,blocks) -> None:
        self.blocks=blocks
    
    def findedges(self):
        edges=[]
        for i in self.blocks:
            uniqedg=0
            for edg in i.edges:
                unique=True
                for j in self.blocks:
                    if i!=j:
                        for edg2 in j.edges:
                            if edg==edg2 or edg==edg2[::-1]:
                                unique=False
                    if unique==False:
                        break
                if unique==True:
                    uniqedg+=1
            if uniqedg==2:
                edges.append(i)
        total=1
        print(len(edges))
        for i in edges:
            total*=i.tilenum
        return total
        


            
            

class block(object):
    def __init__(self,input) -> None:
        super().__init__()
        self.input=input
        self.grid=input[1:]
        self.tilenum=None
        self.edges=[]
        self.parseinput()
    
    def parseinput(self):
        title=self.input[0]
        self.tilenum=int(title.replace('Tile ','').replace(':',''))
        self.edges.append(self.input[1]) #top
        self.edges.append(self.input[-1]) #botom
        self.edges.append(''.join([i[0] for i in self.input[1:]])) #left
        self.edges.append(''.join([i[-1] for i in self.input[1:]])) #right
        print(self.edges)
    
    def pgrid(self):
        print(self.grid)
    def rotate(self):
        pass

        

        



blocklist=[]
for bl in blk:
    blocklist.append(block(bl))
pic=picture(blocklist)
ans=pic.findedges()
print(ans)