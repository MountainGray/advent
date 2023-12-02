from advent import get_input, solution_timer

def parse_data(inp):
    games = {}
    for line in inp:
        _, id, *_= line.split()
        id = int(id.strip(":"))
        matches = line.split(":")[1].split(";")
        matches = list(map(lambda x: x.split(","), matches))
        games[id] = {}
        for idx, match in enumerate(matches):
            r = 0
            g = 0
            b = 0

            for draws in match:
                num, color = draws.split()
                match color:
                    case "red":
                        r = int(num)
                    case "green":
                        g = int(num)
                    case "blue":
                        b = int(num)

            games[id][idx] = (r, g, b)
    return games

@solution_timer(2023, 2, 1)
def part_one(inp):
    games = parse_data(inp)
    red = 12
    green = 13
    blue = 14
    ans = 0
    for key, value in games.items():
        val = True
        for match in value.values():
            if match[0] > red or match[1] > green or match[2] > blue:
                val = False
                break
        if val:
            ans += key
    return ans

@solution_timer(2023, 2, 2)
def part_two(inp):
    games = parse_data(inp)
    ans = 0
    for _, value in games.items():
        mr = max(map(lambda x: x[0], value.values()))
        mg = max(map(lambda x: x[1], value.values()))
        mb = max(map(lambda x: x[2], value.values()))
        ans += mr * mg * mb
    return ans


if __name__ == '__main__':
    inp = get_input(2023, 2)
    part_one(inp)
    part_two(inp)
