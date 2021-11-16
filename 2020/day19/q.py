file= open('Day19/input.txt')
lines=file.read().splitlines()
prerules=lines[:139]
messages=lines[140:]
rulebook={}
for rule in prerules:
    parts=rule.split(': ')
    number=int(parts[0])
    rules=[]
    if '|' in parts[1]:
        options=parts[1].split(' | ')
        first=options[0].split(' ')
        second=options[1].split(' ')
        rules.append([int(i) for i in first])
        rules.append([int(i) for i in second])
    elif '"'in parts[1]:
        rul=parts[1]
        rul.replace(' ','')
        rules.append(rul[1])
    else:
        rules=[int(i) for i in parts[1].split(' ')]
    rulebook[number]=rules

print(rulebook)

def consume(string,rn):
    rule=rulebook[rn]
    if isinstance(rule[0], str): #terminal statement
        if string[0]==rule:
            return len(rule)
        else:
            return -1
    elif isinstance(rule[0], list): # list op
        acc=0   
        for rs in rule:
            ret=consume(string[acc:],rs)
            if ret==-1:
                acc-=1
            else:
                acc+=ret
    else: #single/doubleop
        acc=0
        for rs in rule:
            ret=consume(string[acc:],rs)
            if ret==-1:
                acc-=1
            else:
                acc+=ret
    return -1

acc=0
for i in messages:
    acc+= 1 if consume(i,0)==len(i) else 0

print(acc)
