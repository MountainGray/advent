from advent import get_input, solution_timer
import json


@solution_timer(2015, 12, 1)
def part_one(input_data: list[str]):
    data = json.loads("".join(input_data))

    def recur_sum(data, red_check: bool = False) -> int:
        if isinstance(data, list):
            return sum(map(recur_sum, data))
        elif isinstance(data, dict):
            total = 0
            for key, val in data.items():
                total += recur_sum(key)
                total += recur_sum(val)
            return total
        elif isinstance(data, int):
            return data
        else:
            return 0
    return recur_sum(data)


@solution_timer(2015, 12, 2)
def part_two(input_data: list[str]):
    data = json.loads("".join(input_data))

    def recur_sum(data, red_check: bool = False) -> int:
        if isinstance(data, list):
            return sum(map(recur_sum, data))
        elif isinstance(data, dict):
            total = 0
            for key, val in data.items():
                if val == "red":
                    return 0
                if key == "red":
                    return 0
                total += recur_sum(key)
                total += recur_sum(val)
            return total
        elif isinstance(data, int):
            return data
        else:
            return 0
    return recur_sum(data, True)


if __name__ == "__main__":
    inp = get_input(2015, 12)
    part_one(inp)
    part_two(inp)
