from advent import solution_timer, get_input
import string

@solution_timer(2018, 5, 1)
def part_one(inp):
    poly = inp[0]
    #poly = "dabAcCaCBAcCcaDA"
    update = True
    i = 0
    while update:
        update = False
        i = 0
        while i < len(poly) - 1:
            x, y = poly[i], poly[i+1]
            if x.lower() == y.lower() and x != y:
                poly = poly[:i] + poly[i+2:]
                update = True
            else:
                i += 1
    return len(poly)
        



@solution_timer(2018, 5, 2)
def part_two(inp):
    ans = 20000
    for i in string.ascii_lowercase:
        poly = inp[0]
        poly = poly.replace(i, "")
        poly = poly.replace(i.upper(), "")
        update = True
        while update:
            update = False
            i = 0
            while i < len(poly) - 1:
                x, y = poly[i], poly[i+1]
                if x.lower() == y.lower() and x != y:
                    poly = poly[:i] + poly[i+2:]
                    update = True
                else:
                    i += 1
        ans = min(ans, len(poly))
    return ans

if __name__ == "__main__":
    inp = get_input(2018, 5)
    part_one(inp)
    part_two(inp)
                

