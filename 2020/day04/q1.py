input=open('Day4/input.txt','r')
linesin=input.read().splitlines()
valid=0
checking=""
mustcontain=["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
for i in range(len(linesin)):
    if(linesin[i]==""):
        #check
        total=[]
        vals=checking.split()
        for i in vals:
            total+=i.split(":")
        if len(total)>=14:
            passes=True
            for i in mustcontain:
                if total.count(i)==0:
                    passes=False
            for k, val in enumerate(total):
                if(val=="byr") and (int(total[k+1])<1920 or int(total[k+1])>2002):
                    passes=False
                elif(val=="iyr") and (int(total[k+1])<2010 or int(total[k+1])>2020):
                    passes=False
                elif (val=="eyr") and (int(total[k+1])<2020 or int(total[k+1])>2030):
                    passes=False
                elif (val=="hgt"):
                    if total[k+1][-2:]=="cm" and (int(total[k+1][:-2])<150 or int(total[k+1][:-2])>193):
                        passes=False
                    elif total[k+1][-2:]=="in" and (int(total[k+1][:-2])<59 or int(total[k+1][:-2])>76):
                        passes=False
                    else:
                        if total[k+1][-2:]!="cm" and total[k+1][-2:]!="in":
                            passes=False
                elif(val=="hcl"):
                    if total[k+1][0]!="#":
                        passes=False
                    else:
                        code=total[k+1][1:]
                        if(len(code)!=6):
                            passes=False
                        else:
                            for i in code:
                                if not i.isnumeric() and not i.islower():
                                    passes=False
                elif(val=="ecl"):
                    colors=["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                    if colors.count(total[k+1])==0:
                        passes=False
                elif(val=="pid"):
                    if len(total[k+1])!=9:
                        passes=False
            if passes==True:
                valid+=1
        checking=""
    else:
        checking+=linesin[i] +" "

print(checking)
total=[]
vals=checking.split()
for i in vals:
    total+=i.split(":")
if len(total)>=14:
    passes=True
    for i in mustcontain:
        if total.__contains__(i)==False:
            passes=False
    if passes==True:
        valid+=1
print(valid)

