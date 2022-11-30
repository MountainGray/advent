from advent import get_input, solution_timer
import numpy as np

@solution_timer(2015, 6, 1)
def part_one(input_data: list[str]):
    commands = parse_input(input_data)
    grid = np.zeros((1000, 1000), int)

    for operation, (x1, y1, x2, y2) in commands:
        if operation == 0:
            grid[x1:x2+1, y1:y2+1] = 1
        elif operation == 1:
            grid[x1:x2+1, y1:y2+1] = 0
        else:
            grid[x1:x2+1, y1:y2+1] ^= 1

    return np.sum(grid)


@solution_timer(2015, 6, 2)
def part_two(input_data: list[str]):
    commands = parse_input(input_data)
    grid = np.zeros((1000, 1000), int)

    for operation, (x1, y1, x2, y2) in commands:
        if operation == 0:
            grid[x1:x2+1, y1:y2+1] += 1
        elif operation == 1:
            grid[x1:x2+1, y1:y2+1] -= 1
            grid[grid<0] = 0
        else:
            grid[x1:x2+1, y1:y2+1] += 2

    return np.sum(grid)


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
    
