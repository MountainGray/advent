from advent import get_input, solution_timer, submit
from collections import defaultdict


@solution_timer(2023, 5, 1)
def part_one(inp):
    seeds = list(map(int, inp[0].split()[1:]))
    maps = inp[1:]
    aa = []

    for m in maps:
        tl = []
        ranges = m.split("\n")[1:]
        for r in ranges:
            end, start, dist = map(int, r.split())
            tl.append((start, end, dist))
        aa.append(tl)
    
    def traverse(seed):
        for m in aa:
            for s, n, r in m:
                if seed >= s and seed <= s + r - 1:
                    seed = seed - s + n
                    break
        return seed

    a = min(map(traverse, seeds))
    return a


@solution_timer(2023, 5, 2)
def part_two(inp):
    seeds = list(map(int, inp[0].split()[1:]))
    ranges = [(v1, v1 + v2- 1) for v1, v2 in zip(seeds[::2], seeds[1::2])]

    maps = inp[1:]
    aa = []

    for m in maps:
        tl = []
        m = m.split("\n")[1:]
        for r in m:
            end, start, dist = map(int, r.split())
            tl.append((start, end, dist))
        aa.append(tl)
    
    print(len(ranges))
    print(len(*aa.values()))
        

    
    def traverse_range(r: tuple[int, int], mappings: list[list[tuple[int, int, int]]]):
        low, high = r
        if (low == 0):
            print("fuck")
        if len(mappings) == 0:
            print(low,high)
            return low
        mval = []
        for start, end, dist in mappings[0]:
            if start<= low <= start + dist - 1 and start <= high <= start + dist -1: # fully in mapping
                return traverse_range((low - start + end, high - start + end), mappings[1:])
            elif start<= low <= start + dist - 1: # only low contained
                mval.append(
                    traverse_range((low - start + end, end + dist - 1), mappings[1:])
                )
                low = start + dist # remove captured range
            elif start <= high <= start + dist -1: # end in range
                mval.append(
                    traverse_range((end, high - start + end), mappings[1:])
                )
                high = start - 1
            elif low < start and start + dist - 1 < high:
                mval.append(traverse_range((end, end+dist-1), mappings[1:]))
                mval.append(traverse_range((low,start-1), mappings))
                mval.append(traverse_range((start+dist,high), mappings))
            mval.append(traverse_range((low,high), mappings[1:]))
                
        return min(mval)
            

    ans = min([traverse_range(r, aa) for r in ranges])
    return ans





if __name__ == "__main__":
    test = get_input(2023, 5, filename="test.txt", split_char="\n\n")
    print("Test:")
    part_one(test)
    part_two(test)
    exit()

    print("inp:")
    inp = get_input(2023, 5, split_char="\n\n")
    ans = part_one(inp)
    #submit(2023, 5, 1, ans)
    ans = part_two(inp)
    #submit(2023, 5, 2, ans)

