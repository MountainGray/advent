file=open("Day8/in2.txt","r")
lines=file.read().splitlines()
print(len(lines))
#chunks=file.read.split("\n\n")
acc=0
used=[]
checkpoint=None
moves=[]
for line in lines:
    func=line.split(" ")
    moves.append([func[0],int(func[1])])
print(moves)

    

def findend(i,used=[],run=0,changed=0):
    if i not in used:
        if i>len(lines)-1:
            print("made it")
            print(run)
            print(changed)
        elif changed==0:
            if moves[i][0]=="nop":
                news=used.copy()
                news.append(i)
                findend(i+1,news,run,0)
                print("branch")
                findend(i+moves[i][1],news,run,1)
            if moves[i][0]== "jmp":
                news=used.copy()
                news.append(i)
                findend(i+1,news,run,1)
                findend(i+moves[i][1],news,run,0)
            else:
                news=used.copy()
                news.append(i)
                findend(i+1,news,run+moves[i][1],0)
        else:
            if moves[i][0]=="nop":
                news=used.copy()
                news.append(i)
                findend(i+1,news,run,changed)
            if moves[i][0]=="jmp":
                news=used.copy()
                news.append(i)
                findend(i+moves[i][1],news,run,changed)
            else:
                news=used.copy()
                news.append(i)
                findend(i+1,news,run+moves[i][1],changed)
        
findend(0)

