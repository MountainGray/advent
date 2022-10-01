from advent import get_input, solution_timer


@solution_timer(2015, 6, 1)
def part_one(input_data: list[str]):
    commands = parse_input(input_data)
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for operation, (x1, y1, x2, y2) in commands:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if operation == 0:
                    grid[x][y] = 1
                elif operation == 1:
                    grid[x][y] = 0
                else:
                    grid[x][y] = 1 if grid[x][y] == 0 else 0

    return sum(sum(row) for row in grid)


@solution_timer(2015, 6, 2)
def part_two(input_data: list[str]):
    commands = parse_input(input_data)
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for operation, (x1, y1, x2, y2) in commands:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if operation == 0:
                    grid[x][y] += 1
                elif operation == 1:
                    grid[x][y] = max(0, grid[x][y] - 1)
                else:
                    grid[x][y] += 2

    return sum(map(sum, grid))


def parse_input(input_data: list[str]) -> list[tuple[int, tuple[int, int, int, int]]]:
    commands = []
    for line in input_data:
        if "turn on" in line:
            command = 0
        elif "turn off" in line:
            command = 1
        else:  # toggle
            command = 2
        points = line.split(" ")
        points = tuple(map(int, points[-3].split(",") + points[-1].split(",")))
        command = (command, points)
        commands.append(command)
    return commands


if __name__ == "__main__":
    inp = get_input(2015, 6)
    part_one(inp)
    part_two(inp)
