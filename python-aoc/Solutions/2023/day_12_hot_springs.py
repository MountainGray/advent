from advent import get_input, solution_timer
from functools import cache

@cache
def recur_arrangements(record: str, groups: tuple[int, ...]) -> int:
    if len(groups) == 0:
        return 1 if all([x != "#" for x in record]) else 0
    elif len(record) == 0:
        return 0

    recur_sum = 0
    cur_group_len = groups[0]

    for idx, val in enumerate(record):
        if val == ".":
            continue

        if idx + cur_group_len > len(record):
            return recur_sum

        if idx + cur_group_len < len(record) and record[idx + cur_group_len] == "#":
            if val == "#":
                return recur_sum
        elif all([x != "." for x in record[idx : idx + cur_group_len]]):
            recur_sum += recur_arrangements(record[idx + cur_group_len + 1 :], groups[1:])
            if val == "#":
                return recur_sum
        else:
            if val == "#":
                return recur_sum
    return recur_sum


@solution_timer(2023, 12, 1)
def part_one(inp):
    ans = 0
    for line in inp:
        record, groups = line.split()
        groups = tuple(map(int, groups.split(",")))
        ans += recur_arrangements(record, groups)
    return ans


@solution_timer(2023, 12, 2)
def part_two(inp):
    ans = 0
    for line in inp:
        record, groups = line.split()
        groups = tuple(map(int, groups.split(","))) * 5
        record = (record + "?") * 4 + record
        ans += recur_arrangements(record, groups)
    return ans


if __name__ == "__main__":
    inp = get_input(2023, 12)
    part_one(inp)
    part_two(inp)
