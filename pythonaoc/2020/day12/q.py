file = open('Day12/input.txt','r')
lines=file.read().splitlines()
directs=[]
for line in lines:
    directs.append([line[0],int(line[1:])])

class boat(object):
    def __init__(self,directions) -> None:
        self.directions=directions
        self.position=self.distmanhat(directions)
    def getmandis(self):
        return self.position
    def distmanhat(self, directions):
        direction=0
        x=0
        y=0
        for i in directions:
            if i[0]=='N':
                y+=i[1]
            elif i[0]=='S':
                y-=i[1]
            elif i[0]=='E':
                x+=i[1]
            elif i[0]=='W':
                x-=i[1]
            elif i[0]=='F':
                if direction==90:
                    y+=i[1]
                elif direction==270:
                    y-=i[1]
                elif direction==0:
                    x+=i[1]
                elif direction==180:
                    x-=i[1]
            elif i[0]=='R':
                direction=(direction-i[1])%360
            elif i[0]=='L':
                direction=(direction+i[1])%360
        return abs(x)+abs(y)
boaty=boat(directs)
ans=boaty.getmandis()
print(ans)
class waypoint(object):
    def __init__(self, directions):
        self.directions=directions
        self.x=10
        self.y=1
    def makeboatinstructions(self):
        instructions=[]
        for i in self.directions:
            if i[0]=='N':
                self.y+=i[1]
            elif i[0]=='S':
                self.y-=i[1]
            elif i[0]=='E':
                self.x+=i[1]
            elif i[0]=='W':
                self.x-=i[1]
            elif i[0]=='R':
                temp=self.y
                if i[1]==90:
                    self.y=-self.x
                    self.x=temp
                if i[1]==180:
                    self.y=-self.y
                    self.x=-self.x
                if i[1]==270:
                    self.y=self.x
                    self.x=-temp
            elif i[0]=='L':
                temp=self.y
                if i[1]==90:
                    self.y=self.x
                    self.x=-temp
                if i[1]==180:
                    self.y=-self.y
                    self.x=-self.x
                if i[1]==270:
                    self.y=-self.x
                    self.x=temp
            elif i[0]=='F':
                if self.x>=0:
                    instructions.append(['E',abs(self.x)*i[1]])
                else:
                    instructions.append(['W',abs(self.x)*i[1]])
                    
                if self.y>=0:
                    instructions.append(['N',abs(self.y)*i[1]])
                else:
                    instructions.append(['S',abs(self.y)*i[1]])
        return instructions
                
way = waypoint(directs)
new_directs=way.makeboatinstructions()
better_boaty=boat(new_directs)
ans2=better_boaty.getmandis()
print(ans2)



                    

        

