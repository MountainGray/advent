fl=open('Day20/input.txt')
blocks=fl.read().split('\n\n')
blk=[]
for i in blocks:
    blk.append(i.splitlines())

class picture(object):
    def __init__(self,blocks) -> None:
        self.blocks=blocks
        self.edges=[]
        self.findmatches()
        self.findedges()
    
    def makeimage(self):#compile image here
        start=self.edges[0]
        start.x=0
        start.y=0
        start.orient()

    def findmatches(self):
        for i in self.blocks:
            for edg in i.edges:
                for j in self.blocks:
                    if i!=j:
                        for edg2 in j.edges:
                            if edg==edg2 or edg==edg2[::-1]:
                                i.addn(j,edg)
                                break

    def findedges(self):
        for i in self.blocks:
            if i.matches==2:
                self.edges.append(i)

        
            

class block(object):
    def __init__(self,input) -> None:
        super().__init__()
        self.grid=input[1:]
        self.tilenum=self.ftilenum(input[0])    
        #for edge fetching
        self.edges=[]
        self.top=None
        self.bot=None
        self.left=None
        self.right=None
        self.findedges()

        #manage connections
        self.matches=0
        self.T=None
        self.B=None
        self.L=None
        self.R=None

        #var for grid matching
        self.x=None
        self.y=None
    
    def ftilenum(self, str): #set num for q1
        self.tilenum=int(str.replace('Tile ','').replace(':',''))

    def findedges(self): # call to reorient edges
        self.top=self.grid[0] #top
        self.bot=self.grid[-1] #botom
        self.left=''.join([i[0] for i in self.grid[1:]]) #left
        self.right=''.join([i[-1] for i in self.grid[1:]]) #right
        self.edges=[]
        self.edges.append(self.top)
        self.edges.append(self.bot)
        self.edges.append(self.left)
        self.edges.append(self.right)
        
    def addn(self,block,edge):
        matchto=block.edgeside(edge)
        if edge==self.top or edge[::-1]==self.top:
            self.T=block
        elif edge==self.bot or edge[::-1]==self.bot:
            self.B=block
        elif edge==self.left or edge[::-1]==self.left:
            self.L=block
        else:
            self.R=block
        self.matches+=1
    
    def rotateto(self,edge,side): # rotate until side requested ==edge
        if side=='top':
            while self.top!=edge:
                self
    
    #grid methods
    def flipv(self):
        newgrid=self.grid.copy()
        for i in range(9,-1,-1):
            newgrid[i]=self.grid[9-i]
        self.grid=newgrid
        temp=self.top
        self.top=self.bot
        self.bot=temp
        self.findedges()

    def fliph(self):
        newgrid=[]
        for i in self.grid:
            newgrid.append(i[::-1])
        self.grid=newgrid
        temp=self.right
        self.right=self.left
        self.left=temp
        self.findedges()

    def rotr(self):
        newgrid=[]
        for i in range(10):
            newgrid.append(''.join([j[i]for j in self.grid])[::-1])
        self.grid=newgrid
        self.findedges()

    def rotl(self):
        newgrid=[]
        for i in range(10):
            newgrid.append(''.join([j[9-i]for j in self.grid]))
        self.grid=newgrid
        self.findedges()

    def edgeside(self, edge)-> str: #poss garbage
        if edge==self.top or edge[::-1]==self.top:
            return 'top' 
        elif edge==self.bot or edge[::-1]==self.bot:
            return 'bot' 
        elif edge==self.left or edge[::-1]==self.left:
            return 'left' 
        else:
            return 'right'


    def pgrid(self):
        print('---------')
        for i in self.grid:
            print('['+i+']')

blocklist=[]
for bl in blk:
    blocklist.append(block(bl))

'''
tester=blocklist[0]
#tester.pgrid()
#tester.flipv()
tester.pgrid()
tester.fliph()
tester.pgrid()
tester.rotl()
tester.pgrid()
tester.rotr()
tester.pgrid()
'''