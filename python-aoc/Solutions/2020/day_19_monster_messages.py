rules, messages= open('2020/day19/inp.txt').read().split('\n\n')

rulebook = {}
for rule in rules.split('\n'):
    num, logic = rule.split(': ')
    num = int(num)
    if "\"" in logic:
        print(logic)
        rulebook[num] = logic[1]
    elif "|" in logic:
        rulebook[num] = tuple(tuple(int(x) for x in part.split(" ")) for part in logic.split(' | '))
    else:
        rulebook[num] = tuple([int(x) for x in logic.split(" ")])

print(rulebook)

def consume(rule, message)-> str:
    origional = message
    if type(rule) == str:
        if rule == message[0]:
            return message[1:]
        else:
            return message
    if type(rule) == int:
        return consume(rulebook[rule], message)
    elif type(rule[0]) == tuple:
        return min((consume(rule_option, message) for rule_option in rule))
    else:
        for rule_option in rule:
            message = consume(rule_option, message)
        if message == "":
            return message
        else:
            return origional


total = 0
for message in messages.split('\n'):
    if consume(rulebook[0], message) == "":
        total += 1

print(total)