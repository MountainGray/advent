inp = open("2015/day07/input.txt").read().split("\n")
routes = {}

for line in inp:
    split = line.split(" ")
    routes[split[-1]] = split[:-2]


def expr_eval(expr: list):
    if len(expr) == 1:
        return determine_val(expr[0])
    elif len(expr) == 2:
        return ~determine_val(expr[1])
    else:
        a = determine_val(expr[0])
        b = determine_val(expr[2])
        if expr[1] == "AND":
            return a & b
        elif expr[1] == "OR":
            return a | b
        elif expr[1] == "LSHIFT":
            return a << b
        elif expr[1] == "RSHIFT":
            return a >> b


def determine_val(val):
    if val.isdigit():
        return int(val)
    elif type(routes[val]) != int:
        routes[val] = expr_eval(routes[val])
        return routes[val]
    else:
        return routes[val]


p1 = determine_val("a")
print(p1)


for line in inp:
    split = line.split(" ")
    routes[split[-1]] = split[:-2]

routes["b"] = p1

p2 = determine_val("a")

print(p2)
