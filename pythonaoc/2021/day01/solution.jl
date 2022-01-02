inp = open(f->read(f, String),"2021/day01/input.txt","r")
letnums = map(f-> parse(Int,f), split(inp,"\n"))
total = 0
for i in range(1,length = length(letnums) -1)
    if letnums[i]<letnums[i+1]
        global total += 1
    end
end
println("P1:",total)
total = 0
for i in range(1, length = length(letnums) -3)
    if letnums[i]<letnums[i+3]
        global total += 1
    end
end
print("P2:",total)