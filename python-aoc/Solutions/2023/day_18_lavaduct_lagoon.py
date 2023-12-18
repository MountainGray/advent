from advent import get_input, solution_timer


def general(points):
    area, j = 0, len(points) - 1
    for i in range(len(points)):
        xi, yi = points[i]
        xj, yj = points[j]
        area += (xi + xj) * (yj - yi)
        j = i

    peremiter = 0
    for p1, p2 in zip(points, points[1:]):
        x1, y1 = p1
        x2, y2 = p2
        peremiter += abs(x1 - x2) + abs(y1 - y2)

    return (area // 2) + (peremiter // 2) + 1


@solution_timer(2023, 18, 1)
def part_one(inp):
    direx = []
    for line in inp:
        d, n, c = line.split()
        n = int(n)
        direx.append((d, n, c))
    x, y = 0, 0
    points = [(0, 0)]
    for d, n, c in direx:
        match d:
            case "R":
                x += n
            case "L":
                x -= n
            case "U":
                y -= n
            case "D":
                y += n
        points.append((x, y))
    points.reverse()
    return general(points)


@solution_timer(2023, 18, 2)
def part_two(inp):
    direx = []
    for line in inp:
        c = line.split()[-1][2:-1]
        n, d = c[:-1], c[-1]
        n = int(n, 16)
        direx.append((d, n))

    x, y = 0, 0
    points = [(0, 0)]
    for d, n in direx:
        match d:
            case "0":
                x += n
            case "2":
                x -= n
            case "3":
                y -= n
            case "1":
                y += n
        points.append((x, y))
    points.reverse()
    return general(points)


if __name__ == "__main__":
    inp = get_input(2023, 18)
    part_one(inp)
    part_two(inp)
