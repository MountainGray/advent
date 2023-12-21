from advent import get_input, solution_timer


@solution_timer(2023, 19, 1)
def part_one(inp):
    rules, data = inp
    rb = {}
    for rule in rules.splitlines():
        key, quals = rule.split("{")
        operations = []
        quals = quals[:-1].split(",")
        for qual in quals:
            if ":" in qual:
                operations.append((qual.split(":")[0], qual.split(":")[1]))
            else:
                operations.append(qual)

        rb[key] = operations

    vs = []
    for line in data.splitlines():
        line = line[1:-1].split(",")
        val = [int(i[2:]) for i in line]
        vs.append(val)

    ans = 0
    for x, m, a, s in vs:
        cop = "in"
        while True:
            print(cop, end=" ")
            rules = rb[cop]
            for rule in rules:
                if isinstance(rule, tuple):
                    cond, nkey = rule
                    if eval(cond, {"x": x, "m": m, "a": a, "s": s}):
                        cop = nkey
                        break
                else:
                    cop = rule
                    break
            if cop == "A" or cop == "R":
                break
        if cop == "A":
            ans += x + m + a + s
    return ans


@solution_timer(2023, 19, 2)
def part_two(inp):
    rules, data = inp
    rb = {}
    for rule in rules.splitlines():
        key, quals = rule.split("{")
        operations = []
        quals = quals[:-1].split(",")
        for qual in quals:
            if ":" in qual:
                operations.append((qual.split(":")[0], qual.split(":")[1]))
            else:
                operations.append(qual)

        rb[key] = operations

    constraints = [(1, 4000) for _ in range(4)]

    winranges = []

    idxn = {"x": 0, "m": 1, "a": 2, "s": 3}

    def recur_rdict(key, constraints, path=[]):
        path = path + [key]
        if key == "A":
            winranges.append(constraints)
            #print(key, constraints, path)
            return
        elif key == "R":
            return
        rules = rb[key]
        for rule in rules:
            if isinstance(rule, tuple):
                cond, nkey = rule
                if ">" in cond:
                    target, val = cond.split(">")
                    val = int(val)
                    offset = idxn[target]
                    low, high = constraints[offset]
                    if high < val:
                        continue
                    elif low <= val < high:
                        constraints = (
                            constraints[:offset]
                            + [(low, val)]
                            + constraints[offset + 1 :]
                        )
                        nconstraints = (
                            constraints[:offset]
                            + [(val + 1, high)]
                            + constraints[offset + 1 :]
                        )
                        recur_rdict(nkey, nconstraints, path)
                    elif val < low:
                        recur_rdict(nkey, constraints, path)
                        break
                elif "<" in cond:  # x < 1416
                    target, val = cond.split("<")
                    val = int(val)
                    offset = idxn[target]
                    low, high = constraints[offset]
                    if val < low:
                        continue
                    elif low < val <= high:
                        constraints = (
                            constraints[:offset]
                            + [(val, high)]
                            + constraints[offset + 1 :]
                        )
                        nconstraints = (
                            constraints[:offset]
                            + [(low, val - 1)]
                            + constraints[offset + 1 :]
                        )
                        recur_rdict(nkey, nconstraints, path)
                    elif high < val:
                        recur_rdict(nkey, constraints, path)
                        break
            else:
                recur_rdict(rule, constraints, path)

    recur_rdict("in", constraints)


    ans = 0
    print("Summin")
    for wr in winranges:
        tmp = 1
        for low, high in wr:
            tmp *= high - low + 1
        ans += tmp
    return ans


if __name__ == "__main__":
    inp = get_input(2023, 19, filename="19_evil.in", split_char="\n\n")
    #part_two(inp)
    part_two(inp)
