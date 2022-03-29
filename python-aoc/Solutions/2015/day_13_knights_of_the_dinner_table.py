from advent import get_input, solution_timer
from itertools import permutations


@solution_timer(2015, 13, 1)
def part_one(input_data: list[str]):
    relationships = parse_input(input_data)
    max_happyness = 0
    for perm in permutations(relationships.keys()):
        total_happyness = 0
        for idx, person in enumerate(perm):
            total_happyness += relationships[person][perm[(idx - 1) % len(perm)]]
            total_happyness += relationships[person][perm[(idx + 1) % len(perm)]]
        max_happyness = max(max_happyness, total_happyness)

    return max_happyness


@solution_timer(2015, 13, 2)
def part_two(input_data: list[str]):
    relationships = parse_input(input_data)
    for person in relationships.keys():
        relationships[person]["jacob"] = 0
    relationships["jacob"] = {person: 0 for person in relationships.keys()}

    max_happyness = 0
    for perm in permutations(relationships.keys()):
        total_happyness = 0
        for idx, person in enumerate(perm):
            total_happyness += relationships[person][perm[(idx - 1) % len(perm)]]
            total_happyness += relationships[person][perm[(idx + 1) % len(perm)]]
        max_happyness = max(max_happyness, total_happyness)

    return max_happyness


def parse_input(input_data: list[str]) -> dict[str, dict[str, int]]:
    relationships = {}
    for line in input_data:
        line = line.split()
        person = line[0]
        sign = 1 if line[2] == "gain" else -1
        happiness_delta = sign * int(line[3])
        neighbour = line[-1][:-1]
        if person not in relationships:
            relationships[person] = {}
        relationships[person][neighbour] = happiness_delta

    return relationships


if __name__ == "__main__":
    inp = get_input(2015, 13)
    part_one(inp)
    part_two(inp)
