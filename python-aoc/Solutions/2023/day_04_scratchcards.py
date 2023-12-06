from advent import get_input, solution_timer
from collections import defaultdict


@solution_timer(2023, 4, 1)
def part_one(inp):
    vals = []
    ans = 0
    for line in inp:
        l = line.split(":")[1]
        l = l.split("|")
        v = []
        for i in l:
            nums = i.split()
            nums = set(map(int, nums))
            v.append(nums)
        vals.append(v)
    for idx, i in enumerate(vals):
        # length of intersection of all sets
        val = len(set.intersection(*i))
        if val > 0:
            ans += 2** (val-1)



    return ans

@solution_timer(2023, 4, 2)
def part_two(inp):
    vals = []
    ans = 0
    nvals = {}
    nvals = defaultdict(lambda: 1, nvals)
    for line in inp:
        l = line.split(":")[1]
        l = l.split("|")
        v = []
        for i in l:
            nums = i.split()
            nums = set(map(int, nums))
            v.append(nums)
        vals.append(v)
    for idx, i in enumerate(vals):
        # length of intersection of all sets
        val = len(set.intersection(*i))
        if val > 0:
            print(idx, val)
            for nkey in range(1,val+1):
                nvals[idx + nkey] += nvals[idx] 
        nvals[idx]

    ans = sum(nvals.values())
    print(nvals)
    print(ans)
    return ans



if __name__ == '__main__':
    inp = get_input(2023, 4)
    #part_one(inp)
    part_two(inp)