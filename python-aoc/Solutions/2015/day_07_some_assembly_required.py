from advent import get_input, solution_timer
from typing import Any


@solution_timer(2015, 7, 1)
def part_one(input_data: list[str]):
    routes = parse_input(input_data)
    answer = solution(routes, "a")
    return answer


@solution_timer(2015, 7, 2)
def part_two(input_data: list[str], p1_answer: int):
    routes = parse_input(input_data)
    routes["b"] = p1_answer
    answer = solution(routes, "a")
    return answer


def parse_input(input_data: list[str]) -> dict[str, Any]:
    routes = {}
    for line in input_data:
        split = line.split(" ")
        routes[split[-1]] = split[:-2]

    return routes


def solution(routes, wire):
    def expr_eval(expr: list):
        if len(expr) == 1:
            return determine_val(expr[0])
        elif len(expr) == 2:
            return ~determine_val(expr[1])
        else:
            a = determine_val(expr[0])
            b = determine_val(expr[2])
            if expr[1] == "AND":
                return a & b
            elif expr[1] == "OR":
                return a | b
            elif expr[1] == "LSHIFT":
                return a << b
            elif expr[1] == "RSHIFT":
                return a >> b

    def determine_val(val):
        if val.isdigit():
            return int(val)
        elif type(routes[val]) != int:
            routes[val] = expr_eval(routes[val])
            return routes[val]
        else:
            return routes[val]

    signal = determine_val(wire)
    return signal


if __name__ == "__main__":
    puzzle_input = get_input(2015, 7)
    p1_answer = part_one(puzzle_input)
    part_two(puzzle_input, p1_answer)
