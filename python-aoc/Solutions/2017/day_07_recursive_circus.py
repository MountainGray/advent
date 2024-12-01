from advent import get_input, solution_timer

@solution_timer(2017,7, 1)
def part_one(inp):
    leafs = []
    nodes = []
    for x in inp:
        if "->" in x:
            x, rest = x.split(" -> ")
            name, num = x.split()
            num = int(num[1:-1])
            children = rest.split(", ")
            nodes.append((name, num, children))
        else: # leaf 
            name, num = x.split()
            num = int(num[1:-1])
            leafs.append((name, num))
    
    for (name, _, _) in nodes:
        if not any([name in x[2] for x in nodes]):
            return name

@solution_timer(2017,7, 2)
def part_two(inp):
    leafs = {}
    nodes = {}
    for x in inp:
        if "->" in x:
            x, rest = x.split(" -> ")
            name, num = x.split()
            num = int(num[1:-1])
            children = rest.split(", ")
            nodes[name] = (num, children)
        else: # leaf 
            name, num = x.split()
            num = int(num[1:-1])
            leafs[name] = num
    

    root = None
    for (name, _, _) in nodes.keys():
        if not any([name in x for x in nodes.values()]):
            root = name
            return
    
    weight = {}
    def find_weight(node):
        if node in leafs:
            w = leafs[node]
            weight[node] = w
            return w 
        else:
            v, children = nodes[node]
            w = v
            for c in children:
                w += find_weight(c)
            
            weight[node] = w
            return w
    for node in nodes:



if __name__ == "__main__":
    inp = get_input(2017, 7)
    part_one(inp)
    part_two(inp)