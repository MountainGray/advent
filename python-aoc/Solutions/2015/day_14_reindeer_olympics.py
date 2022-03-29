from advent import get_input, solution_timer


TIME = 2503


@solution_timer(2015, 14, 1)
def part_one(input_data: list[str]):
    reindeer_stats = parse_input(input_data)
    max_distance = 0

    for (reindeer, speed, endurance, rest) in reindeer_stats:
        total = (speed * endurance) * (TIME // (endurance + rest)) + (
            speed * min((TIME % (endurance + rest)), endurance)
        )
        max_distance = max(max_distance, total)
    return max_distance


@solution_timer(2015, 14, 2)
def part_two(input_data: list[str]):
    reindeer_stats = parse_input(input_data)
    scoreboard = {reindeer[0]: 0 for reindeer in reindeer_stats}

    for t in range(1, TIME + 1):
        max_distance = 0
        point_earners = []
        for (reindeer, speed, endurance, rest) in reindeer_stats:
            total = (speed * endurance) * (t // (endurance + rest)) + (
                speed * min((t % (endurance + rest)), endurance)
            )
            if total > max_distance:
                point_earners = [reindeer]
                max_distance = max(max_distance, total)
            elif total == max_distance:
                point_earners.append(reindeer)

        for reindeer in point_earners:
            scoreboard[reindeer] += 1

    return max(scoreboard.values())


def parse_input(input_data: list[str]):
    reindeer_stats = []
    for line in input_data:
        line = line.split()
        reindeer = line[0]
        speed = int(line[3])
        endurance = int(line[6])
        rest = int(line[-2])
        reindeer_stats.append((reindeer, speed, endurance, rest))
    return reindeer_stats


if __name__ == "__main__":
    inp = get_input(2015, 14)
    part_one(inp)
    part_two(inp)

