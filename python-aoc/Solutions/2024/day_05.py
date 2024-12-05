from advent import get_input, solution_timer

@solution_timer(2024, 5, 1)
def part_one(inp: list[str]):
    a, b = inp
    rules= []
    for i in a.split("\n"):
        x,y = i.split("|")
        x,y = int(x), int(y)
        rules.append((x,y))
    
    ans = 0
    for i in b.split("\n"):
        n = [int(x) for x in i.split(",")]
        valid = True
        for (x,y) in rules:
            if x in n and y in n and n.index(x) > n.index(y):
                valid = False
                break
        if valid:
            ans += n[len(n)//2]
    return ans


@solution_timer(2024, 5, 1)
def part_two(inp: list[str]):
    a, b = inp
    rules= []
    for i in a.split("\n"):
        x,y = i.split("|")
        x,y = int(x), int(y)
        rules.append((x,y))
    
    ans = 0
    for i in b.split("\n"):
        n = [int(x) for x in i.split(",")]
        valid = True
        for (x,y) in rules:
            if x in n and y in n and n.index(x) > n.index(y):
                valid = False
                break
        if valid:
            continue
        else:
            changed = True
            while changed:
                changed = False
                for (x,y) in rules:
                    if x in n and y in n and n.index(x) > n.index(y):
                        n[n.index(x)], n[n.index(y)] = n[n.index(y)], n[n.index(x)]
                        changed = True

            middle = n[len(n)//2]
            ans += middle
        
    return ans

if __name__ == "__main__":
    inp = get_input(2024, 5, split_char="\n\n")
    part_one(inp)
    part_two(inp)
