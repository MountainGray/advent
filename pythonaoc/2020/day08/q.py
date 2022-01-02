file=open("Day8/input.txt","r")
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
        elif changed==0:
            if moves[i][0]=="nop":
                news=used.copy()
                news.append(i)
                findend(i+1,news,run,0)
                findend(i+moves[i][1],news,run,1)
            elif moves[i][0]== "jmp":
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
                findend(i+1,news,run,1)
            elif moves[i][0]=="jmp":
                news=used.copy()
                news.append(i)
                findend(i+moves[i][1],news,run,1)
            else:
                news=used.copy()
                news.append(i)
                findend(i+1,news,run+moves[i][1],1)
    else:
        print("found end")
        
findend(0)

