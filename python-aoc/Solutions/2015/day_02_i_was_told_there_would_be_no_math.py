from advent.load_input import get_input
from advent.timer import solution_timer


@solution_timer(2015, 2, 1)
def part_one(input_data: list[str]):
    dimensions = parse_input(input_data)
    paper = 0
    for x, y, z in dimensions:
        paper += 2 * x * y + 2 * y * z + 2 * x * z + min(x * y, y * z, x * z)
    return paper


@solution_timer(2015, 2, 2)
def part_two(input_data: list[str]):
    dimensions = parse_input(input_data)
    ribbon = 0
    for x, y, z in dimensions:
        ribbon += 2 * x + 2 * y + x * y * z
    return ribbon


def parse_input(input_data: list[str]) -> list[list[int]]:
    dimensions: list[list[int]] = []
    for line in input_data:
        dimensions.append(sorted(map(int, line.split("x"))))
    return dimensions


if __name__ == "__main__":
    data = get_input(2015, 2)
    part_one(data)
    part_two(data)
