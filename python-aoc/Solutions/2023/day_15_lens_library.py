from advent import get_input, solution_timer


@solution_timer(2023, 15, 1)
def part_one(inp):
    inp = "".join(inp).split(",")
    ans = 0
    for i in range(len(inp)):
        tsum = 0
        for char in inp[i]:
            tsum += ord(char)
            tsum *= 17
            tsum %= 256
        ans += tsum
    return ans


@solution_timer(2023, 15, 2)
def part_two(inp):
    inp = "".join(inp).split(",")
    ans = 0
    stacks = [[] for _ in range(256)]
    for box in inp:
        tsum = 0
        for char in box:
            if char == "=" or char == "-":
                break
            tsum += ord(char)
            tsum *= 17
            tsum %= 256
        if "=" in box:
            tag, val = box.split("=")
            val = int(val)
            nb = False
            for idx, obox in enumerate(stacks[tsum]):
                if obox[0] == tag:
                    stacks[tsum][idx] = [tag, val]
                    nb = True
                    break
            if not nb:
                stacks[tsum].append((tag, val))
        elif "-" in box:
            tag, val = box.split("-")
            for box in stacks[tsum]:
                if box[0] == tag:
                    stacks[tsum].remove(box)
                    break

    for ids, stack in enumerate(stacks):
        for idb, box in enumerate(stack):
            v = (1+ids) * (1+idb) * box[1]
            ans += v
    
    
    return ans

if __name__ == "__main__":
    inp = get_input(2023, 15)
    part_one(inp)
    part_two(inp)
