from advent import get_input, solution_timer


@solution_timer(2015, 9, 1)
def part_one(input_data: list[str]):
    nodes = parse_input(input_data)

    def recur_min_path(node: str, distance: int, visited: list[str]) -> int:
        min_distance = 1000
        if len(visited) == len(nodes):
            return distance
        for end, dist in nodes[node]:
            if end not in visited:
                dist_total = recur_min_path(end, distance + dist, visited+[end])
                min_distance = min(min_distance, dist_total)
        return min_distance

    distance = 1000
    for node in nodes.keys():
        distance = min(distance, recur_min_path(node, 0, [node]))

    return distance


@solution_timer(2015, 9, 2)
def part_two(input_data: list[str]):
    nodes = parse_input(input_data)

    def recur_max_path(node: str, distance: int, visited: list[str]) -> int:
        max_distance = 0
        if len(visited) == len(nodes):
            return distance
        for end, dist in nodes[node]:
            if end not in visited:
                dist_total = recur_max_path(end, distance + dist, visited+[end])
                max_distance = max(max_distance, dist_total)
        return max_distance

    distance = 0
    for node in nodes.keys():
        distance = max(distance, recur_max_path(node, 0, [node]))

    return distance


def parse_input(input_data: list[str]) -> dict[str, list[tuple[str, int]]]:
    nodes = {}
    for line in input_data:
        start, _, end, _, distance = line.split()
        if start not in nodes:
            nodes[start] = []
        nodes[start].append((end, int(distance)))
        if end not in nodes:
            nodes[end] = []
        nodes[end].append((start, int(distance)))

    return nodes


if __name__ == "__main__":
    inp = get_input(2015, 9)
    part_one(inp)
    part_two(inp)
