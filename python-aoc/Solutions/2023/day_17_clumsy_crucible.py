from advent import get_input, solution_timer
from advent.helpers import defaultdict
mmm = 1000000

@solution_timer(2023, 17, 1)
def part_one(inp):
    inp = [[int(x) for x in line] for line in inp]
    mx, my = len(inp[0]), len(inp)
    end = (mx-1, my-1)
    optm = defaultdict(lambda: mmm)
    opt_dir = defaultdict(lambda: (mmm, 0) )
    # x, y, dx, dy, movement, cost
    positions = set()
    positions.add((0, 1, 0, 1, 2, 0))
    positions.add((1, 0, 1, 0, 2, 0))

    while len(positions) > 0:
        x, y, dx, dy, movement, cost = positions.pop()
        if x < 0 or y  < 0 or x >= mx or y>= my:
            continue
        cost += inp[y][x]
        max_cost= optm[end]
        opt_cost= optm[(x, y)]
        if cost < opt_cost:
            optm[(x, y)] = cost
        if cost >= max_cost:
            continue
        max_cdir, mleft = opt_dir[(x,y, dx, dy)]
        if cost >= max_cdir and movement <= mleft:
            continue
        opt_dir[(x,y, dx, dy)] = (cost, movement)

        if (x, y) == end:
            positions = set(filter(lambda x: x[5] < cost, positions))

        else:
            if movement > 0:
                positions.add((x+dx, y+dy, dx, dy, movement-1, cost))
            match (dx, dy):
                case (0, -1):
                    positions.add((x+1, y, 1, 0, 2, cost))
                    positions.add((x-1, y, -1, 0, 2, cost))
                case (0, 1):
                    positions.add((x+1, y, 1, 0, 2, cost))
                    positions.add((x-1, y, -1, 0, 2, cost))
                case (1, 0):
                    positions.add((x, y+1, 0, 1, 2, cost))
                    positions.add((x, y-1, 0, -1, 2, cost))
                case (-1, 0):
                    positions.add((x, y+1, 0, 1, 2, cost))
                    positions.add((x, y-1, 0, -1, 2, cost))

    return optm[end]


@solution_timer(2023, 17, 2)
def part_two(inp):
    inp = [[int(x) for x in line] for line in inp]
    mx, my = len(inp[0]), len(inp)
    end = (mx-1, my-1)
    # cost, movementleft, direction
    optm = defaultdict(lambda: mmm)
    opt_dir = defaultdict(lambda: (mmm, 0) )


    # x, y, dx, dy, movement, cost
    positions = set()
    positions.add((0, 1, 0, 1, 9, 0))
    positions.add((1, 0, 1, 0, 9, 0))

    while len(positions) > 0:
        x, y, dx, dy, movement, cost = positions.pop()
        if x < 0 or y  < 0 or x >= mx or y>= my:
            continue
        cost += inp[y][x]
        max_cost= optm[end]
        opt_cost= optm[(x, y)]
        if cost < opt_cost:
            optm[(x, y)] = cost
        if cost >= max_cost:
            continue

        max_cdir, mleft = opt_dir[(x,y, dx, dy)]

        if cost > max_cdir and movement < mleft:
            continue
        opt_dir[(x,y, dx, dy)] = (cost, movement)

        if (x, y) == end:
            positions = set(filter(lambda x: x[5] < cost, positions))
        else:
            if movement > 0:
                positions.add((x+dx, y+dy, dx, dy, movement-1, cost))
            if movement >= 7:
                continue
            else:
                match (dx, dy):
                    case (0, -1):
                        if x + 4 < mx:
                            positions.add((x+1, y, 1, 0, 9, cost))
                        if x - 4 >= 0:
                            positions.add((x-1, y, -1, 0, 9, cost))
                    case (0, 1):
                        if x + 4 < mx:
                            positions.add((x+1, y, 1, 0, 9, cost))
                        if x - 4 >= 0:
                            positions.add((x-1, y, -1, 0, 9, cost))
                    case (1, 0):
                        if y + 4 < my:
                            positions.add((x, y+1, 0, 1, 9, cost))
                        if y - 4 >= 0:
                            positions.add((x, y-1, 0, -1, 9, cost))
                    case (-1, 0):
                        if y + 4 < my:
                            positions.add((x, y+1, 0, 1, 9, cost))
                        if y - 4 >= 0:
                            positions.add((x, y-1, 0, -1, 9, cost))
    return optm[end]

if __name__ == "__main__":
    inp = get_input(2023, 17)
    part_one(inp)
    part_two(inp)
