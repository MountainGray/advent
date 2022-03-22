from advent.load_input import get_input
from advent.timer import solution_timer


@solution_timer(2015, 3, 1)
def part_one(input_data: list[str]):
    directions = input_data[0]
    houses = {0+0j}
    pos = 0+0j
    # Part 1
    for dr in directions:
        if dr == "^":
            pos += 1j
        elif dr == "v":
            pos -= 1j
        elif dr == ">":
            pos += 1
        elif dr == "<":
            pos -= 1
        houses.add(pos)

    return len(houses)


@solution_timer(2015, 3, 2)
def part_two(input_data: list[str]):
    directions = input_data[0]
    santa = 0+0j
    robo_santa = 0+0j
    houses = {0+0j}
    for i, dr in enumerate(directions):
        if i % 2 == 0:
            if dr == "^":
                santa += 1j
            elif dr == "v":
                santa -= 1j
            elif dr == ">":
                santa += 1
            elif dr == "<":
                santa -= 1
            houses.add(santa)
        else:
            if dr == "^":
                robo_santa += 1j
            elif dr == "v":
                robo_santa -= 1j
            elif dr == ">":
                robo_santa += 1
            elif dr == "<":
                robo_santa -= 1
            houses.add(robo_santa)

    return len(houses)


if __name__ == "__main__":
    data = get_input(2015, 3)
    part_one(data)
    part_two(data)
