from typing import List
from advent import get_input, solution_timer


@solution_timer(2015, 1, 1)
def part_one(input_data: List[str]):
    instructions = input_data[0]
    answer = 0
    for direction in instructions:
        if direction == "(":
            answer += 1

        elif direction == ")":
            answer -= 1

    return answer


@solution_timer(2015, 1, 2)
def part_two(input_data: List[str]):
    instructions = input_data[0]
    answer = 0
    for i, direction in enumerate(instructions):
        if direction == "(":
            answer += 1

        elif direction == ")":
            answer -= 1
        if answer == -1:
            return i + 1

    return answer


if __name__ == '__main__':
    data = get_input(2015, 1)
    part_one(data)
    part_two(data)
